from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', views.main_page, name='main_page'),
    path('add-category/', views.add_category, name='add_category'),
    path('display-category/', views.display_category, name='display_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),

    path('addcar/', views.add_car, name='add_car'),
    path('display-car/', views.display_car, name='display_car'),
    path('edit-car/<int:id>/', views.edit_car, name='edit_car'),
    path('delete-car/<int:id>/', views.delete_car, name='delete_car'),

    path('', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),

    path('display-contact/', views.display_contact, name='display_contact'),
    path('delete-contact/<int:id>/', views.delete_contact, name='delete_contact'),

    path('display-enquiry/', views.display_enquiry, name='display_enquiry'),
    path('delete-enquiry/<int:id>/', views.delete_enquiry, name='delete_enquiry'),

    path('display-testdrive/', views.display_testdrive, name='display_testdrive'),
    path('delete-testdrive/<int:id>/', views.delete_testdrive, name='delete_testdrive'),

    path('user-register-details/', views.user_register_details, name='user_register_details'),

    path('listing-request/', views.listing_request, name='listing_request'),

]
