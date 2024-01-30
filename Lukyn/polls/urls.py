from django.urls import path

from . import views

urlpatterns = [
    path('randomnuber/',views.models_list)
    ]
