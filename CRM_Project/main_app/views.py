from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Order


class Index(ListView):
    template_name = 'main_app/index.html'
    model = Order
    context_object_name = 'orders'

