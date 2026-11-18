from django.contrib import admin
from .models import Category, Info, Book, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'pages', 'country', 'language')
    search_fields = ('country', 'language')
    list_filter = ('country', 'language')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'rating', 'author')
    search_fields = ('title', 'author')
    list_filter = ('category', 'rating', 'tags')
    list_display_links = ('id', 'title')
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
