from django.forms import ModelForm
from .models import Order


class NewOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'client', 'unit', ]