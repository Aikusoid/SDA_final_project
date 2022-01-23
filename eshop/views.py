from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView

from eshop.forms.accounts import RegistrationForm, UserProfileForm
from eshop.models import Paint, Author, Category, OrderItem, Order, UserProfile


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

    def get(self, request, pk):
        context = {
            'paint': Paint.objects.get(pk=pk),
            'pk': pk,
        }
        return TemplateResponse(request, 'paint_detail.html', context=context)


class AddToCartView(DetailView, SuccessMessageMixin):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        print(pk)
        item = get_object_or_404(Paint, pk=pk)

        order, _ = Order.objects.get_or_create(
            user=UserProfile.objects.get(user=request.user),
            ordered=False,
        )

        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            ordered=False,
            order=order,
        )

        if item.is_available:
            if not created:
                order_item.quantity += 1
                order_item.save(update_fields=['quantity', ])
                messages.success(request, 'Added to cart!')
            else:
                order_item.quantity = 1
                order_item.save(update_fields=['quantity', ])
                messages.success(request, "Added to cart!")

            item.quantity -= 1
            item.save(update_fields=['quantity', ])
            return redirect("paint:detail", pk=pk)

        else:
            messages.error(request, 'This paint is no longer available.')

            return redirect("paint:detail", pk=pk)


class CartDetailView(DetailView):
    model = Order
    template_name = "cart_detail.html"

    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        items = self.model.objects.get(user=user_profile).orderitem_set.all()
        total_price = 0
        total_items = 0
        for item in items:
            total_price += item.item.price * item.quantity
            total_items += item.quantity

        context = {
            'items': items,
            'total_price': total_price,
            'total_items': total_items,
        }
        return TemplateResponse(request, "cart_detail.html", context=context)


class RegistrationView(FormMixin, TemplateView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'{form.cleaned_data["username"]} created')
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Something wrong')
            return TemplateResponse(request, 'accounts/registration.html', context={'form': form})


class LoginView(FormMixin, TemplateView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Log in successfully')
            return redirect('homepage')

        messages.error(request, 'Wrong Credentials')
        return redirect('auth:login')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Log out successfully')
        return redirect('homepage')


class UpdateUserProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    form_class = UserProfileForm
    model = UserProfile
    success_message = 'Successfully updated profile'
    success_url = reverse_lazy('homepage')
