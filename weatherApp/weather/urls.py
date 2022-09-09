from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('some_page/', views.page, name='page'),
]