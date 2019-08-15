from django.urls import include, path, re_path
from second_app import views

urlpatterns = [
    path('', views.index),
    path('help/', views.help),
    path('users/', views.users),
]
