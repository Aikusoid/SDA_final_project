from django.contrib import admin

from eshop.models import Paint, Category, Artist, OrderItem, Order, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'description', 'category', 'price', 'created', 'size', 'image']


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'date_of_birth']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ordered', 'start_date', 'ordered_date']


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paint, PaintAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
