from django.forms import ModelForm
from .models import Order, Client, Unit, Brand, Model, UnitType, Part, Services
from django import forms

class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', ]

        widgets = {
            'defect': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Defect description', 'rows': 3, 'cols': 40}),

        }

class OrderDetailForm(ModelForm):
    class Meta:
        model = Order
        fields = ['defect', 'diagnostic_result', 'finally_price', 'services', 'repair_stage',  ]

        widgets = {
            'defect': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 24, }),
            'diagnostic_result': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, }),
            'finally_price': forms.TextInput(attrs={'class': 'form-control', }),
            'repair_stage': forms.Select(attrs={'class': 'form-control', }),
            'services': forms.SelectMultiple(attrs={'class': 'form-control', })

        }


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone_number']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your surname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number', 'data-mask': '123456'})
        }

class NewUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['brand', 'model', 'serial_number', 'type']

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit model'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
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

class EditClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'surname': forms.TextInput(attrs={'class': 'form-control', }),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
        }

class NewPartForm(ModelForm):

    class Meta:
        model = Part
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.TextInput(attrs={'class': 'form-control', })
        }

class NewServiceForm(ModelForm):

    class Meta:
        model = Services
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'price': forms.TextInput(attrs={'class': 'form-control', })
        }