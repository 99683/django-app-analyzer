from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('upload/', views.upload_file,name='upload'),

    path('overview/', views.overview, name='overview'),

    path('visualize/', views.visualize, name='visualize'),

    path('statistics/', views.statistics, name='statistics'),

]

