from django.contrib import admin
from .models import Post, Comment, PageSettings

from django.db import models
from suit_ckeditor.widgets import CKEditorWidget

# Посты
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                'author',
                'title',
                'text',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

#  Комментарии
admin.site.register(Comment)

# Настройки страницы
@admin.register(PageSettings)
class PageConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                'name_website',
                'descriptor_website',
            ),
        }),
    )