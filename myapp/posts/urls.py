from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^details/(?P<id>\d+)/$',views.details,name="details"),
    url(r'^add/',views.addPost,name="addPost"),
    url(r'^search/',views.search,name="addPost"),
    url(r'^contact/',views.contact,name="addPost"),
    url(r'^complaint',views.complaint,name="complaint"),
    url('^business',views.business,name="business")

 
]