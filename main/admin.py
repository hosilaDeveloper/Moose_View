from django.contrib import admin
from .models import Author, Tag, Article, Comment, About

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'crested')
    list_display_links = ('id', 'title', 'created')
    search_fields = ['title',]
    filter_horizontal = ['tags',]


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(About)
