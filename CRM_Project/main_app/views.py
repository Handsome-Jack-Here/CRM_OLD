from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, View
from .models import Order, Client, Unit, Brand, Model, UnitType, RepairStage
from .forms import NewOrderForm, NewClientForm, NewUnitForm, NewBrandForm, NewModelForm, NewUnitTypeForm, \
    OrderDetailForm, EditClientForm
from django.http import HttpResponseRedirect


class Index(ListView):
    template_name = 'main_app/index.html'
    model = Order
    context_object_name = 'orders'


class NewOrder(View):

    def get(self, request):
        default_stage = RepairStage.objects.get(stage='Diagnostic')
        return render(request, 'main_app/add_order.html',
                      context={'order_form': NewOrderForm, 'client_form': NewClientForm, 'unit_form': NewUnitForm,
                               'unit_type_form': NewUnitTypeForm,
                               'brand_form': NewBrandForm, 'model_form': NewModelForm})

    def post(self, request):
        new_order = NewOrderForm(request.POST)
        # new_client = NewClientForm(request.POST)

        if new_order.is_valid():
            print('Is valid!')

            order = Order(defect=request.POST['defect'], )
            unit = Unit(serial_number=request.POST['serial_number'], )
            client = Client(name=request.POST['name'], surname=request.POST['surname'],
                            phone_number=request.POST['phone_number'])
            client.save()
            order.client = client
            unit.type = UnitType.objects.get(id=request.POST['type'])
            unit.save()



            model = Model(model=request.POST['model'])
            brand = Brand(brand=request.POST['brand'])

            model_exists = False
            for exist_model in Model.objects.all():

                if model.model == exist_model.model:
                    model_exists = True
                    unit.model = exist_model
                    break

            if not model_exists:
                model.save()
                unit.model = model

            brand_exists = False
            for exist_brand in Brand.objects.all():

                if brand.brand == exist_brand.brand:
                    brand_exists = True
                    unit.brand = exist_brand
                    break

            if not brand_exists:
                brand.save()
                unit.brand = brand

            unit.save()
            order.unit = unit
            order.repair_stage = RepairStage.objects.get(stage='Diagnostic')
            order.save()

            return HttpResponseRedirect('/')


class GetOrder(View):

    def get(self, request, val: int):
        this_order = Order.objects.get(id=val)
        this_client = this_order.client
        this_unit = this_order.unit
        form = OrderDetailForm(instance=this_order)
        return render(request, 'main_app/order_detail.html', context={'order': form, 'client': this_client, 'unit': this_unit })

    def post(self, pk: int):
        pass


class EditClient(View):

    def get(self, request, val: int):
        this_client = Client.objects.get(id=val)
        client_form = EditClientForm(instance=this_client)
        return render(request, 'main_app/edit_client.html', context={'client': client_form, })


    def post(self, request, val: int):
        this_client = Client.objects.get(id=val)
        client_form = EditClientForm(request.POST,  instance=this_client)
        if client_form.is_valid():
            client_form.save()
            return HttpResponseRedirect('/')
