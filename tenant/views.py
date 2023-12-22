from django.shortcuts import render, get_object_or_404
from .models import Tenant

def tenant_list(request):
    """listing all tenants"""
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def tenant_profile(request, tenant_id):
    """tenant detail"""
    tenant = get_object_or_404(Tenant, id=tenant_id)
    leases = tenant.lease_set.select_related('unit')

    context = {
        'tenant': tenant,
        'leases': leases,
    }
    return render(request, 'tenant_profile.html', context)

