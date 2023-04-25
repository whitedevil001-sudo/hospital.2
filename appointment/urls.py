from django.contrib import admin
from django.urls import path
from .views import parchi_list, parchi_create

urlpatterns=[

    path('parchi/',parchi_list),
    path('parchi/new/',parchi_create),

]