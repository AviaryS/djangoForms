from django.urls import path
from engine import views


urlpatterns = [
    path('', views.form),
    path('appointment/', views.index),
    path('order/', views.order)
]