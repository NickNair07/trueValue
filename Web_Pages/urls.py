from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-cars/', views.all_cars, name='all_cars'),
    path('cars/<car_name>', views.cars, name='cars'),
    path('car-detail/<int:id>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]