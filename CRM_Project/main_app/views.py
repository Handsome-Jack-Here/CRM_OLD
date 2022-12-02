from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, View
from .models import Order, Client, Unit, Brand, Model, UnitType
from .forms import NewOrderForm, NewClientForm, NewUnitForm, NewBrandForm, NewModelForm, NewUnitTypeForm
from django.http import HttpResponseRedirect


class Index(ListView):
    template_name = 'main_app/index.html'
    model = Order
    context_object_name = 'orders'


class OrderDetail(DetailView):
    template_name = 'main_app/order_detail.html'
    model = Order
    context_object_name = 'order'


class NewOrder(View):

    def get(self, request):
        return render(request, 'main_app/add_order.html',
                      context={'order_form': NewOrderForm, 'client_form': NewClientForm, 'unit_form': NewUnitForm,
                               'unit_type_form': NewUnitTypeForm,
                               'brand_form': NewBrandForm, 'model_form': NewModelForm})

    def post(self, request):
        new_order = NewOrderForm(request.POST)
        # new_client = NewClientForm(request.POST)

        if new_order.is_valid():
            order = Order(defect=request.POST['defect'])
            unit = Unit(serial_number=request.POST['serial_number'])
            client = Client(name=request.POST['name'], surname=request.POST['surname'],
                            phone_number=request.POST['phone_number'])
            client.save()
            order.client = client
            order.type_of_unit = UnitType.objects.get(id=request.POST['type_of_unit'])
            unit.brand = Brand.objects.get(id=request.POST['brand'])
            unit.model = Model.objects.get(id=request.POST['model'])
            unit.save()
            order.unit = unit
            order.save()
            return HttpResponseRedirect('/')
