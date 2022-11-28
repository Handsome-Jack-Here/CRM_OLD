from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('order/<int:pk>', views.OrderDetail.as_view(), name='get-order'),
    path('new_order', views.NewOrder.as_view(), name='add-new-order'),


]