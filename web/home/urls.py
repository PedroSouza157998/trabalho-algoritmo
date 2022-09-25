from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name=''),
    path('index/', views.index, name=''),
]
