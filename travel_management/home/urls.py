import django
from django import contrib
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.urls import path,include
from home import views 


admin.site.site_title="ULAA"
admin.site.site_header="ULAA Admin"
admin.site.index_title="Dashboard"
urlpatterns = [
    path('', views.home, name='home'),
    path('availability', views.availability, name='availability'),
    path('accounts/register/',views.register,name='register'),
    path('faq', views.faq, name='faq'),
    path('availabilitydisplay', views.availabilitydisplay, name='availabilitydisplay'),
    path('routes',views.routes,name='routes'),
    path('contact',views.contact,name='Contact'),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('success', views.success, name="success"),
    path('modal', views.modal, name="modal"),
]

