import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Driver, Service, Order, Vehicle, FAQ
from .forms import *

def index(request):
    services = Service.objects.all()
    drivers = Driver.objects.all()
    vehicles = Vehicle.objects.all()
    return render(request, 'polls/index.html', {'title': 'Главная страница', 'drivers': drivers,
                                                'services': services, 'vehicles': vehicles})


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
    drivers = Driver.objects.all()
    vehicles = Vehicle.objects.all()
    return render(request, 'polls/services.html', {'title': 'Услуги', 'drivers': drivers,
                                                'services': services, 'vehicles': vehicles})


def about_us(request):
    return render(request, 'polls/about_us.html', {'title': 'О нас'})

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'polls/faq.html', {'title': 'FAQ',
                                              'faqs': faqs})