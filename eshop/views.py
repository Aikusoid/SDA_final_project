from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
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


