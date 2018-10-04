from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Posts,Tag,EditorsChoice

from .forms import ArticleForm,Deletion_requestForm

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


def business(req):
    return render(req,"posts/fluff/advertisement.html",{})

def search(req):
    return HttpResponse("search disabled. Not enough posts to start indexing engine. Try filtering by tags instead")
    
def contact(req):
    return HttpResponse("contact")

# Create your views here.
def index(req):

    url_path= req.get_full_path()
    #grabs url path
    url_splitted= url_path.split("/")
    url_splitted_non_space_in_arr=[]
    #filters out the slashes

    for i in url_splitted:
         if(i==""):
             print("non")
         else:
             url_splitted_non_space_in_arr.append(i)


    print(url_splitted)
    print(url_splitted_non_space_in_arr)

    

    posts = Posts.objects.filter().order_by('-id')

    paginator= Paginator(posts,5)

    totalPages=paginator.num_pages

    totalPagesArr=[]

    for number in range(totalPages):
        print(number)
        totalPagesArr.append(number+1)
    
    print(totalPagesArr)

    page= req.GET.get("page")

    tag= req.GET.get("cat")

     
    

    

    posts_to_send= paginator.get_page(page)

    if(tag!=None):
        c=Tag.objects.get(pk=tag).posts_set.all()
        posts_to_send=c

    
    



    
    editors_choice= EditorsChoice.objects.values('post').all()

    EditorsPosts=[]

    for ec in editors_choice:
        EditorsPosts.append(Posts.objects.get(pk=ec['post']))
    
    

    
    
    all_tags= Tag.objects.all()
    

    context={
        "posts":posts_to_send,
        "editorspicks":EditorsPosts,
        "title":"Recent Posts",
        "url_full_path":url_path,
        "url_processed":url_splitted_non_space_in_arr,
        "tags":all_tags,
        "totalPaginatedPages":totalPagesArr,
        "currentPage":1
    }


    return render(req,"posts/index.html",context)    

def complaint(req):
    return render(req,'posts/fluff/formal_removal_request.html',{'form':Deletion_requestForm})

def details(req,id):

    url_path= req.get_full_path()
    #grabs url path
    url_splitted= url_path.split("/")
    url_splitted_non_space_in_arr=[]
    #filters out the slashes

    for i in url_splitted:
         if(i==""):
             print("non")
         else:
             url_splitted_non_space_in_arr.append(i)


    print(url_splitted)
    print(url_splitted_non_space_in_arr)

    #also read other posts
    recommendPosts= Posts.objects.exclude(id=id)
    


    post= Posts.objects.get(id=id)
    return render(req,"posts/detail.html",{"post":post
    ,
        "url_full_path":url_path,
        "url_processed":url_splitted_non_space_in_arr,
        "recommend":recommendPosts
        })


def addPost(req):
    form= ArticleForm()

    url_path= req.get_full_path()
    #grabs url path
    url_splitted= url_path.split("/")
    url_splitted_non_space_in_arr=[]
    #filters out the slashes

    for i in url_splitted:
         if(i==""):
             print("non")
         else:
             url_splitted_non_space_in_arr.append(i)


    print(url_splitted)
    print(url_splitted_non_space_in_arr)

    if req.method=="POST":
        postData= req.POST
        print(postData)
        # print(req.FILES["thumbnail"])
        form=ArticleForm(req.POST)
        form.save()

        return redirect("/posts/")

    return render(req,"posts/addPost.html",{'form':form
    ,
        "url_full_path":url_path,
        "url_processed":url_splitted_non_space_in_arr
    })