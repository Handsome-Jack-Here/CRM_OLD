from django.forms import ModelForm
from .models import Order, Client, Unit, Brand, Model


class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', ]


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class NewUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['serial_number', ]


class NewBrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class NewModelForm(ModelForm):

    class Meta:
        model = Model
        fields = '__all__'