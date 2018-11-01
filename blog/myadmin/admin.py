from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# 博客：标题，作者，内容，发布时间，分类（外键），标签（多对多）等
# 标签：标签名称
# 类别：分类名称
# 评论：作者，博客（外键），邮箱，内容，发布时间等。

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category','content','pub')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)


