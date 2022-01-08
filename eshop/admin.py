from django.contrib import admin

from eshop.models import Paint, Category, Author


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'price', 'created', 'size', 'image']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'paint', 'first_name', 'last_name', 'date_of_birth']


admin.site.register(Paint, PaintAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
