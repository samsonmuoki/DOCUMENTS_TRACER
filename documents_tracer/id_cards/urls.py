from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reportid/', views.report_id, name='report_id'),
    path('allids/', views.all_ids, name='all_ids'),
]
