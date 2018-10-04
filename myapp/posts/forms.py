from django.forms import ModelForm
from .models import Posts, Delete_Requested,SuggestATopic

from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model= SuggestATopic
        fields=['topic_title','bigger_description','your_name']

class Deletion_requestForm(ModelForm):
    class Meta:
        model= Delete_Requested
        fields=['post','reason_for_request','user_comment','your_name','your_email']
