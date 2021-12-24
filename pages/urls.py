from django.urls import path
from django_hosts.resolvers import reverse
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('kevin/', views.KevinPageView.as_view(), name='kevin'),

    path('basecontact/', views.basecontactView, name='basecontact'),
]