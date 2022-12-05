from django.forms import ModelForm
from .models import Order, Client, Unit, Brand, Model, UnitType


class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'type_of_unit']

class OrderDetailForm(ModelForm):
    model = Order
    fields = ['defect', 'diagnostic_result', 'client', 'works', 'finally_price', 'client', 'type_of_unit', 'unit', 'repair_stage', ]


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class NewUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['serial_number', 'brand', 'model']


class NewBrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class NewModelForm(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'


class NewUnitTypeForm(ModelForm):
    class Meta:
        model = UnitType
        fields = '__all__'
