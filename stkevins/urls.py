from django.urls import path, include
from stkevins import views

app_name = 'stkevins'

urlpatterns = [
    path('', views.parish_view, name='stkevins'),
    path('fuck/', views.MassesTemplateView.as_view(), name='masses'),
]