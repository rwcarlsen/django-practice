
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/<str:expression>', views.submit, name='submit'),
    path('status/', views.status, name='status'),
    path('fetch/', views.fetch, name='fetch'),
    path('report/', views.report, name='report'),
]
