from django.forms import ModelForm
from .models import Order, Client, Unit, Brand, Model, UnitType
from django import forms

class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'type_of_unit', ]

        widgets = {
            'defect': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Defect description', 'rows': 3, 'cols': 40}),
            'type_of_unit': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unit type'}),

        }

class OrderDetailForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'diagnostic_result', 'client', 'works', 'finally_price', 'client', 'type_of_unit', 'unit', 'repair_stage', ]


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone_number']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your surname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'})
        }

class NewUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['brand', 'model', 'serial_number']

        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unit brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit model'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'})
        }


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
