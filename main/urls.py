from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data', views.data, name='data'),
    path('data/submit', views.submit, name='submit'),
]
