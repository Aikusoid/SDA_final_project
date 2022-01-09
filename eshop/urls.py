from django.urls import path, include

from eshop.views import homepage_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
]
