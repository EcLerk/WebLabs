import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, EmailValidator
from django.db import models
from django.urls import reverse


class Employees(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=30)
    position = models.CharField('должность', max_length=40, default='')
    phone_number = models.CharField('номер телефона', validators=[RegexValidator(r'^\+375?\d{9}$',
                                                                                 "Phone number must be entered in the format: '+999999999'")],
                                    max_length=13, default='+375441111111')
    email = models.EmailField('эл. почта', validators=[EmailValidator('')],
                              default='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Vehicle(models.Model):
    brand = models.CharField('бренд', max_length=20)
    model = models.CharField('модель', max_length=20)
    year = models.IntegerField('год выпуска', validators=[MinValueValidator(1980), MaxValueValidator(2023)])

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}"


class Service(models.Model):
 #   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('наименование услуги', max_length=40)
    description = models.TextField('описание услуги')

    def __str__(self):
        return self.title


class Order(models.Model):
  #  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderDate = models.DateField('время заказа', auto_now=True)
    name = models.CharField('имя', max_length=20, default='USER')
    phone_number = models.CharField('номер телефона', validators=[RegexValidator(r'^\+375?\d{9}$',
                                                                     "Phone number must be entered in the format: '+999999999'")],
                                    max_length=13, default='+375441111111')

    services = models.ManyToManyField(Service)

    def __str__(self):
        return f"заказ №{self.id}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class FAQ(models.Model):
    question = models.TextField('вопрос')
    answer = models.TextField('ответ')
    date = models.DateField('дата добавления', auto_now=True)

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание', default='')
    article = models.TextField('Статья', default='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='')
    date = models.DateField('дата добавления', auto_now=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    description = models.TextField()
    date = models.DateField('дата добавления', auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username} ({self.rating}/5)"

class Coupons(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField()
    promocode = models.CharField('Промокод', max_length=10)

    is_active = models.BooleanField('Активен', default=True)

