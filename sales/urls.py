from django.urls import path
from sales import views

urlpatterns = [
    path('orders/',views.listoders)
]