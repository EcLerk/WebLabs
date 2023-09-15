from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Client, Service, Order


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        client = Client(user=user)
        client.save()

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'services']

class ReviewForm(forms.Form):
    rating = forms.IntegerField(label='Оценка', min_value=1, max_value=5)
    description = forms.CharField(label='Отзыв', widget=forms.Textarea)
