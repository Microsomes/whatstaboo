from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


siteStatus= (
    ('FR', 'Active'),
    ('SO', 'Inactive'),
    ('JR', 'In Selling'),
    ('SR', 'No longer supported'),
)


class app_settings(models.Model):
    site_name=  models.CharField(max_length=300)
    site_description= models.CharField(max_length=300)
    site_logo= models.ImageField(upload_to="media",default="null")
    show_nsfw_posts_without_asking= models.BooleanField(default=False)
    site_owned_by_company_or_name= models.CharField(max_length=400,default="Phase5 productions")
    site_status_is_production= models.CharField(max_length=300,choices=siteStatus)


class Tag(models.Model):
    tag_label= models.CharField(max_length=400)
    total_posts= models.IntegerField(default=0)
    def __str__(self):
        return self.tag_label

class Posts(models.Model):
    title= models.CharField(max_length=200,help_text=" ")
    # body= RichTextUploadingField(blank=True,null=True,help_text=" ")
    body= models.TextField(blank=True,default="---write something")
    created_at = models.DateTimeField(default=datetime.now,blank=True,help_text=" ")
    thumbnail= models.ImageField(upload_to="media",default="null",help_text=" ")

 
    category= models.ManyToManyField(Tag,help_text=" ")

    created_by_name = models.CharField(max_length=200, default="system")

    claps_number= models.BigIntegerField(default="0")

    is_verified= models.BooleanField(default=False)

    is_nsfw= models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="Posts"

    #called before post saves
 
 

class Delete_Requested(models.Model):
    deletionReasons= (
    ('Discriminatory', 'Discriminatory'),
    ('Offensive', 'Offensive'),
    ('Blackmail', 'Blackmail')
 )
    post= models.ForeignKey(Posts,on_delete=models.CASCADE,help_text=" ")
    reason_for_request=models.CharField(choices=deletionReasons,max_length=300,help_text=" ")
    your_name= models.CharField(max_length=300,default="")
    your_email= models.EmailField(max_length=300,default="")
    user_comment= models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.reason_for_request

    class Meta:
        verbose_name_plural="Delete Requested"

class Recommend(models.Model):
    post= models.ForeignKey(Posts,on_delete=models.CASCADE,default=0)


#stores all the id foreign keys of posts that are featured
class EditorsChoice(models.Model):
    post= models.ForeignKey(Posts,on_delete="CASCADE")
    
    def __str__(self):
        return self.post.title
    
    class Meta:
        verbose_name_plural="Editors Choice"

#allow users to suggest a topic
class SuggestATopic(models.Model):
    topic_title= models.CharField(max_length=300)
    bigger_description= models.CharField(blank=True,default="leave blank unless you are compelled",max_length=300)
    your_name= models.CharField(blank=True,default="Leave blank unless you want some credit (:",max_length=300)

    def __str__(self):
        return self.topic_title
    