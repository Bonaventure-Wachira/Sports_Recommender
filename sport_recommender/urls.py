
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form, name='input_form'),
    path('recommended_sport/', views.recommended_sport, name='recommended_sport'),
]
