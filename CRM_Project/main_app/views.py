from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Order, Client
from .forms import NewOrder


class Index(ListView):
    template_name = 'main_app/index.html'
    model = Order
    context_object_name = 'orders'


class OrderDetail(DetailView):
    template_name = 'main_app/order_detail.html'
    model = Order
    context_object_name = 'order'


class NewOrder(CreateView):
    form_class = NewOrder
    model = Order
    template_name = 'main_app/add_order.html'
    success_url = '/'
    context_object_name = 'form'

    # def get_context_data(self, **kwargs):
    #     super(NewOrder, self).get_context_data(**kwargs)

