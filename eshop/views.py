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


# class OrderItemDetailView(DetailView, SuccessMessageMixin):
#     model = OrderItem
#     template_name = 'cart_detail.html'


class AddToCartView(DetailView, SuccessMessageMixin):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        print(pk)
        item = get_object_or_404(Paint, pk=pk)
        order_item = OrderItem.objects.get_or_create(
            item=item,
            ordered=False
        )

        ordered_items = Order.objects.filter(ordered=False)

        # If we already have smth in cart
        if item.is_available:
            if ordered_items.exists():
                order = ordered_items[0]
                # if we have already added this item to cart and want to add more units
                if order.items.filter(pk=pk).exists():
                    order_item.quantity += 1
                    order_item.save(update_fields=['quantity', ])
                    messages.success(request, 'Added to cart!')
                else:
                    order.items.add(order_item)
                    messages.info(request, "Added to cart!")
            else:
                ordered_date = timezone.now()
                order = Order.objects.create(ordered_date=ordered_date)
                order.items.add(order_item)
                messages.success(request, 'Added to cart!')

            item.quantity -= 1
            item.save(update_fields=['quantity', ])
            return redirect("cart:detail", pk=pk)

        else:
            messages.error(request, 'This paint is no longer available.')

            return redirect("paint:detail", pk=pk)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'cart_detail.html'


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
