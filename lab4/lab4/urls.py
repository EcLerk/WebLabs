"""
URL configuration for lab4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from polls.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('singup/', SingUp.as_view(), name='singup'),
    path('orders/', orders, name='orders'),
    path('createorder', create_order, name='create_order'),
    path('ordersuccess/', order_success, name='order_success'),
    path('dogs/', show_dog, name='dogs'),
    path('services/', services, name='services'),
    path('about/', about_us, name='about'),
    path('faq/', faq, name='faq'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('review_form/', create_review, name='review_form'),
    path('reviews/', reviews, name='reviews'),
    path('privacy/', privacy_policy, name='privacy'),
    path('coupons/', coupons, name='coupons'),
    path('some_page/', some_page, name='some_page'),
    path('certificate/', certificate, name = 'certificate'),
    path('text_change/', text_change, name = 'text_change'),
    path('age_calculator/', age_calculator, name = 'age_calculator'),
    path('scroll/', scroll, name = 'scroll'),
    path('interactive_table/', interactive_table, name = 'interactive_table'),
    path('autoplay/', autoplay, name='autoplay'),
    path('associative_array/', associative_array, name='associative_array'),
    path('paralax/', paralax, name='paralax'),
    path('calculator/', calculator, name='calculator')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)