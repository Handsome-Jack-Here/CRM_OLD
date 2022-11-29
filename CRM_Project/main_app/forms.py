from django.forms import ModelForm
from .models import Order, Client


class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'client', 'unit', ]


class NewClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'