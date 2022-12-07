from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('new_order', views.NewOrder.as_view(), name='add-new-order'),
    path('order/<int:val>', views.GetOrder.as_view(), name='get-order'),



]