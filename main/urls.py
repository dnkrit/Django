from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('second/', views.page2, name='page2'),
]
