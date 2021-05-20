
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/<str:expression>', views.submit, name='submit'),
    path('status/', views.status, name='status'),
    path('fetch/<int:client_id>', views.fetch, name='fetch'),
    path('report/<int:job_id>/<str:result>', views.report, name='report'),
]
