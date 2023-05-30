from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('addcar', views.add_car, name='add_car'),
    path('save_car', views.save_car, name='save_car'),
]
