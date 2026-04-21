from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('skill/create/', views.skill_create, name='skill_create'),
    path('skill/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skill/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('skill/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]
