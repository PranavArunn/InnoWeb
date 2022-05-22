from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('edit/', views.Create),
    path('feedback/', views.Feedback),
    path('index/', views.index)
]
