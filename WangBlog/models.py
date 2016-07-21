from django.db import models
from django.contrib import admin
from django import forms
# Create your models here.


#定义表单模型.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')


class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50)
    sex = models.BooleanField(choices=(('m', '男'), ('f', '女'),))

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name='内容')
    time = models.TimeField(verbose_name='时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    img = models.FileField(default='', upload_to='./upload/')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'img')


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(User, UserAdmin)
