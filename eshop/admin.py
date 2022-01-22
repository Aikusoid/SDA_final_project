from django.contrib import admin

from eshop.models import Paint, Category, Author, OrderItem, Order, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'price', 'created', 'size', 'image']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'date_of_birth']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ordered', 'start_date', 'ordered', 'ordered_date']


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paint, PaintAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
