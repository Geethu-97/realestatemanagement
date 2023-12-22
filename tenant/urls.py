from django.urls import path
from .views import tenant_list, tenant_profile

urlpatterns = [
    path('tenants/list', tenant_list, name='tenant_list'),
    path('tenant/<int:tenant_id>/', tenant_profile, name='tenant_profile')
]
