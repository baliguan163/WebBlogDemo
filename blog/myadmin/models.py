from django.db import models
#Create your models here.
#coding=utf-8

# from __future__ import unicode_literals
from django.db import models
#
# 数据库的构建(M）
# 首先，我们分析一个博客系统的功能：
# （1）一个博客可以有多个标签（多对多）
# （2）一个博客可以有多条评论(一对多）
# （3）一个博客只可以有一个类别（多对一）
# 接下来，我们分析关系的属性：

# 博客：标题，作者，内容，发布时间，分类（外键），标签（多对多）等
# 标签：标签名称
# 类别：分类名称
# 评论：作者，博客（外键），邮箱，内容，发布时间等。
# ---------------------

# Create your models here.
class Category(models.Model):  #继承models.Model
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('名称',max_length=16)
    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField('标题',max_length=32)
    author=models.CharField('作者',max_length=16)
    content=models.TextField('内容')
    pub=models.DateField('发布时间',auto_now_add=True)
    category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)  #多对一（博客--类别）
    tag=models.ManyToManyField(Tag,verbose_name='标签')   #(多对多）
    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)#(博客--评论:一对多)
    name=models.CharField('称呼',max_length=16)
    email=models.EmailField('邮箱')
    content=models.CharField('内容',max_length=240)
    pub=models.DateField('发布时间',auto_now_add=True)
    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"
    def __unicode__(self):
        return self.content
