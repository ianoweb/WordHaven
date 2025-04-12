from django.contrib import admin
from . models import Blogs,categories,Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('title',)}
    list_display=['title','is_published','date']
    list_editable = ['is_published']
    list_filter=['is_published']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['message','date','is_approved']
    list_editable = ['is_approved']



admin.site.register(Blogs,BlogAdmin)
admin.site.register(categories)
admin.site.register(Comment,CommentAdmin)