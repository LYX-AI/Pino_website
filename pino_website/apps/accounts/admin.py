from django.contrib import admin

# Register your models here.
from django.contrib import admin#导入 Django 自带的 admin 模块，用于管理后台界面。
from .models import UserPersona, UserProfile

admin.site.register(UserPersona)
admin.site.register(UserProfile)