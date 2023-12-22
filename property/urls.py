from django.urls import path
from .views import PropertyDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail')
]