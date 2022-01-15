from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return f'{self.name}'


class Paint(BaseModel):
    title = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='paints')
    image = models.ImageField(null=False, blank=False, upload_to='./static/products')
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
    works = models.ManyToManyField(Paint, related_name='works')

    def get_detail_url(self):
        return reverse('author:detail', args=[self.pk])


class UserAccount(Person):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, blank=True, upload_to='profile_images')
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    phone = models.IntegerField()


class OrderLine(BaseModel):
    order_item = models.ManyToManyField(Paint, related_name='order_item')
    number_of_products = models.IntegerField()
    cost = models.OneToOneField(Paint, on_delete=models.CASCADE, related_name='cost')

    def total_price(self):
        return self.number_of_products * self.cost


class Order(BaseModel):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    total_cost = models.ForeignKey(OrderLine, on_delete=models.CASCADE, related_name='total_price')
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    date_of_submission = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='Processing')
    '''
    Order lines (entity)
    Client (entity)
    Status (enum)
    '''


