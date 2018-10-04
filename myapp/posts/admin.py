from django.contrib import admin

# Register your models here.

from .models import Posts,Tag, EditorsChoice,Recommend,app_settings,Delete_Requested,SuggestATopic



class PostsAdmin(admin.ModelAdmin):
    # list_display=('title','created_by_name','created_at')

    # search_fields=('title','created_by_name','body',)

    # list_filter=('category','created_by_name')

    # ordering=('created_at',)
    pass


class Delete_RequestedAdmin(admin.ModelAdmin):
    list_display=('your_name','reason_for_request','user_comment')

admin.site.register(Posts,PostsAdmin)
admin.site.register(Tag)
admin.site.register(EditorsChoice)
admin.site.register(Recommend)
admin.site.register(app_settings)
admin.site.register(Delete_Requested,Delete_RequestedAdmin)
admin.site.register(SuggestATopic)

admin.site.site_header = 'Admin@whatstaboo.com'
