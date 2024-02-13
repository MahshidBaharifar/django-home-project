from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class CommentAdminInline(admin.TabularInline):
    fields = ['text', ]
    model= Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable','publish_date','created_time']
    inlines = [CommentAdminInline]


admin.site.register(Post,PostAdmin)


#class CommentAdmin(admin.ModelAdmin):
 #   list_display = ['post','text','created_time']

#admin.site.register(Comment,CommentAdmin)