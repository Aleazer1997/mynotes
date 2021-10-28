from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='route' ),
    path('notes/', views.getNotes, name='route' ),
    path('notes/<str:pk>/', views.getNote, name='route' )
]