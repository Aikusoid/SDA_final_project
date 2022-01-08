from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.pk}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Category(BaseModel):
    name = models.CharField(max_length=512, unique=True, blank=True)
    # parent categories and children categories (tree placement)


class Paint(BaseModel):
    title = models.CharField(max_length=512, unique=True)
    description = models.CharField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    image = models.ImageField(null=False, blank=False, upload_to='products')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created = models.DateField()
    height = models.IntegerField()
    width = models.IntegerField()

    @property
    def size(self):
        return f'{self.height} x {self.width}'

    def __str__(self):
        return f'{self.title}'


class Author(Person):
    paint = models.ManyToManyField(Paint, related_name='paint', through='eshop.Paint')


class UserAccount(Person):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, blank=True, upload_to='profile_images')
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    phone = models.IntegerField()


class OrderLine(BaseModel):
    product = models.ManyToManyField(Paint, related_name='product', through='eshop.Order')
    number_of_products = models.IntegerField()
    price = models.OneToOneField(Paint.price, related_name='price')

    def total_price(self):
        return self.number_of_products * self.price


class Order(BaseModel):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    total_cost = models.OneToOneField(OrderLine, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    date_of_submission = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Processing')
    '''
    Order lines (entity)
    Client (entity)
    Status (enum)
    '''


