from django.db import models
from django.utils import timezone
from solo.models import SingletonModel

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=100, verbose_name='Автор комментария')
    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class PageSettings(SingletonModel, models.Model):
    name_website = models.TextField(verbose_name='Название сайта', max_length=20)
    descriptor_website = models.TextField(verbose_name='Описание сайта', max_length=50)

    def settingsSave(self):
        self.save()

    def __str__(self):
        return 'Настройки конфигурации'

# class HistoryEdit(models.Model):
#     descriptor_edit = models.TextField(verbose_name='Название сайта', max_length=20)
#     descriptor_website = models.TextField(verbose_name='Описание сайта', max_length=50)
#     name_list = 'Настройки конфигурации'
#
#     def settingsSave(self):
#         self.save()
#
#     def __str__(self):
#         return self.name_list