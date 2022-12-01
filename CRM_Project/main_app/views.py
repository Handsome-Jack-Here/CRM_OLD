from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, View
from .models import Order, Client, Unit, Brand, Model
from .forms import NewOrderForm, NewClientForm, NewUnitForm, NewBrandForm, NewModelForm
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
                               'brand_form': NewBrandForm, 'model_form': NewModelForm})

    def post(self, request):
        new_order = NewOrderForm(request.POST)

        if new_order.is_valid():
            client = Client(name=request.POST['name'])
            order = Order(defect=request.POST['defect'])
            brand = Brand(brand=request.POST['brand'])
            model = Model(model=request.POST['model'])
            unit = Unit(serial_number=request.POST['serial_number'])
            client.save()
            brand.save()
            model.save()
            print(type(brand))
            unit.brand = brand
            unit.model = model
            unit.save()
            order.client = client
            order.unit = unit

            order.save()
            return HttpResponseRedirect('/')

# class NewOrder(CreateView):
#     form_class = NewOrderForm
#     model = Order
#     template_name = 'main_app/add_order.html'
#     success_url = '/'
#     context_object_name = 'form'
#
#     def get_context_data(self, **kwargs):
#         context = super(NewOrder, self).get_context_data(**kwargs)
#         context['new_client'] = NewClientForm()  # self.request.POST
#         client = context['new_client']
#         if self.request.method == 'POST':
#             context['new_client'] = NewClientForm(self.request.POST).save()
#         else:
#             context['new_client'] = NewClientForm
#
#         return context
