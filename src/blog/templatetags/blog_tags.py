# -*- coding: utf-8 -*-
from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count

#自定义模板标签代码写在 blog_tags.py 文件中。其实模板标签本质上就是一个 Python 函数，因此按照 Python 函数的思路来编写模板标签的代码就可以了

#Django 在模板中还不知道该如何使用它。为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，必须按照 Django 的规定注册这个函数为模板标签，方法如下
#这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 get_recent_posts 装饰为 
#register.simple_tag。这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
#Django 1.9 后才支持 simple_tag 模板标签，如果你使用的 Django 版本小于 1.9，你将得到一个错误
register = template.Library()

#这个函数的功能是获取数据库中前 num 篇文章，这里 num 默认为 5。
#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    #return Category.objects.all()
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)