from datetime import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin


class BaseModel(models.Model):
    created = models.DateTimeField(
        # auto_now_add=True,
        default=datetime.utcnow,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=256, )
    last_name = models.CharField(max_length=256)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.pk}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, blank=True, upload_to='profile_images')
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    phone = models.IntegerField()


class Category(BaseModel):
    name = models.CharField(max_length=512, unique=True, blank=True)
    # parent categories and children categories (tree placement)

    def __str__(self):
        return f'{self.name}'


class Artist(Person):
    country = models.CharField(max_length=30)

    def get_detail_url(self):
        return reverse('artist:detail', args=[self.pk])


class Paint(BaseModel):
    title = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512, blank=True, default='')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='paintings')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='paints')
    image = models.ImageField(null=False, blank=False, upload_to='./static/products')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField()
    height = models.IntegerField()
    width = models.IntegerField()
    quantity = models.IntegerField(default=1)

    @property
    def size(self):
        return f'{self.height} x {self.width}'

    @property
    def is_available(self):
        if self.quantity > 0:
            return True

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('paint:detail', args=[self.pk])

    def get_add_to_cart_url(self):
        return reverse('cart:add', args=[self.pk])

    def get_remove_from_cart_url(self):
        return reverse('cart:remove', args=[self.pk])


class OrderItem(BaseModel):
    item = models.ForeignKey(Paint, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)

    @property
    def total_item_price(self):
        return self.quantity * self.item.price


class Order(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=False, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)
