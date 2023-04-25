from django.contrib import admin
from django.urls import path
from .views import doctor_list, doctor_create

urlpatterns=[

    path('doctor/',doctor_list),
    path('doctor/new/',doctor_create),

]