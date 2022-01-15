from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import DetailView, FormView, TemplateView
from django.urls import reverse_lazy

from eshop.models import Paint, Author, Category


def homepage_view(request):
    context = {
        'paintings': Paint.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all(),
        'prices_start_from': Paint.objects.all().count(),
    }
    return TemplateResponse(request, 'homepage.html', context=context)


def authorDetailView(request, pk):
    context = {
        'paintings': Paint.objects.all(),
        'author': Author.objects.get(pk=pk),
    }

    return TemplateResponse(request, 'author_detail.html', context=context)


class CategoryListView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        context = {
            'categories': Category.objects.all(),
        }
        return TemplateResponse(request, 'category_list.html', context=context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get(self, request, pk):
        context = {
            'paintings': Paint.objects.filter(category=pk).all(),
            'category': Category.objects.get(pk=pk),
        }
        return TemplateResponse(request, 'category_detail.html', context=context)


class PaintDetailView(DetailView):
    model = Paint
    template_name = 'paint_detail.html'
