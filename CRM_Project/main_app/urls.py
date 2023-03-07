from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(),name='home'),
    path('new_order', views.NewOrder.as_view(), name='add-new-order'),
    path('order/<int:val>/', views.GetOrder.as_view(), name='get-order'),
    path('order/client-edit/<int:val>', views.EditClient.as_view(), name='edit-client'),
    path('order-edit/', views.OrderEdit.as_view()),



]