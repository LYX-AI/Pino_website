from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
class UserProfile：定义了一个模型类 UserProfile，表示与数据库中某个表相关联的对象。
models.Model：这是 Django 提供的基类，用于将 Python 类映射到数据库表。
20250126添加
'''
class UserInterest(models.Model):
   name=models.CharField(max_length=64,unique=True)
   normalized_name=models.CharField(max_length=64,unique=True)
   def __str__(self):
      return self.name
class UserPersona(models.Model):
   name=models.CharField(max_length=64,unique=True)#姓名是唯一的
   normalized_name=models.CharField(max_length=64,unique=True)
   description=models.CharField(max_length=200)
   def __str__(self):
      return self.name

class UserProfile(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
   is_full_name_displayed=models.BooleanField(default=True)#字段类型：BooleanField，表示一个布尔值字段（True 或 False）。default=True：如果没有显式设置值，默认值为 True。用途：用于指示是否显示用户的全名。
   #detail
   bio=models.CharField(max_length=500,blank=True,null=True)
   #max_length=500：最多可以存储 500 个字符。
   #blank=True：表示该字段在表单中可以留空（前端验证）。
   #null=True：表示该字段在数据库中可以存储 NULL 值。
   #用于存储用户的个人简介
   website=models.URLField(max_length=200,blank=True,null=True)
   #用途：存储用户的个人网站地址
   persona=models.ForeignKey(UserPersona,on_delete=models.SET_NULL,blank=True,null=True)
   interest=models.ManyToManyField(UserInterest,blank=True)