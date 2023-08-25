from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('add_dish', views.add_dish, name='add_dish'),
    path('remove_dish/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('update/<int:dish_id>/', views.update, name='update'),
    path('take_order/<int:dish_id>/',views.take_order,name="take_order"),
    path('display_orders',views.display_orders,name="display_orders"),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]