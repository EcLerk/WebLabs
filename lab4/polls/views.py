import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Employees, Service, Order, Vehicle, FAQ, News, Review, Coupons
from .forms import *

def index(request):
    services = Service.objects.all()
    drivers = Employees.objects.all()
    vehicles = Vehicle.objects.all()
    article = News.objects.all().last()
    return render(request, 'polls/index.html', {'title': 'Главная страница', 'drivers': drivers,
                                                'services': services, 'vehicles': vehicles, 'article': article})


def login(request):
    return render(request, 'polls/../templates/registration/login.html')


def logged_out(request):
    return render(request, 'registration/logged_out.html')


class SingUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'polls/signup.html'


def orders(request):
    orders = Order.objects.all()
    return render(request, 'polls/orders.html', {'orders': orders})


def order_success(request):
    return render(request, 'polls/order_success.html')

def create_order(request):
    form = OrderForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            selected_values = form.cleaned_data['services']
            order = Order()
            #order = form.save(commit=False)

            order.name = name
            order.phone_number = phone_number
            order.save()
            order.services.set(selected_values)

            return render(request, 'polls/order_success.html')
        else:
            form = OrderForm()

    return render(request, 'polls/create_order.html', {'form': form})

def show_dog(request):
    resp = requests.get('https://dog.ceo/api/breeds/image/random')

    img_url = resp.json()['message']
    print(img_url)
    return render(request, 'polls/dogs.html', {'img_url': img_url})

def services(request):
    services = Service.objects.all()
    drivers = Employees.objects.all()
    vehicles = Vehicle.objects.all()
    return render(request, 'polls/services.html', {'title': 'Услуги', 'drivers': drivers,
                                                'services': services, 'vehicles': vehicles})


def about_us(request):
    return render(request, 'polls/about_us.html', {'title': 'О нас'})

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'polls/faq.html', {'title': 'FAQ',
                                              'faqs': faqs})

def contacts(request):
    employees = Employees.objects.all()
    return render(request, 'polls/contacts.html', {'title': 'Контакты',
                                              'employees': employees})

def news(request):
    news = News.objects.all()
    return render(request, 'polls/news.html', {'title':'Новости',
                                               'news': news})

def show_post(request, post_id):
    article = News.objects.get(id=post_id)
    return render(request, 'polls/article.html', {'title':f'Статья {post_id}',
                                               'article': article})

def create_review(request):
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            description = form.cleaned_data['description']

            review = Review(rating=rating, description=description)
            review.user = user
            review.save()

            return redirect('success_review_page')
    else:
        form = ReviewForm()

    return render(request, 'polls/review_form.html', {'form':form})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'polls/reviews.html', {'title': 'Отзывы','reviews':reviews})

def privacy_policy(request):
    return render(request, 'polls/privacy_policy.html', {'title': 'Политика конфиденциальности',
                                                         'reviews': reviews})

def coupons(request):
    coupons = Coupons.objects.all()
    return render(request, 'polls/coupons.html', {'title': 'Купоны',
                                                  'coupons': coupons})

def some_page(request):
    return render(request, 'polls/some_page.html', {'title': 'some_page'})

def certificate(request):
    return render(request, 'polls/certificate.html', {'title': 'cerificate'})

def text_change(request):
    return render(request, 'polls/js/text_change.html', {'title': 'text'})

def age_calculator(request):
    return render(request, 'polls/js/age_calculator.html', {'title': 'age'})

def scroll(request):
    return render(request, 'polls/js/scroll.html', {'title': 'scroll'})

def interactive_table(request):
    return render(request, 'polls/js/interactive_table.html', {'title': 'text'})

def autoplay(request):
    return render(request, 'polls/js/autoplay.html', {'title': 'autoplay'})

def associative_array(request):
    return render(request, 'polls/js/associative_array.html', {'title': 'associative_array'})

def paralax(request):
    return render(request, 'polls/js/paralax.html', {'title': 'paralax'})

def calculator(request):
    return render(request, 'polls/js/calculator.html', {'title': 'calculator'})
