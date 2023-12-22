from django.contrib import admin

from tenant.models import Lease, Tenant

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Lease)

