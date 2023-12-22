import uuid
from django.db import models

from property.models import Unit

# Create your models here.
class Tenant(models.Model):
    id = models.AutoField(primary_key=True)
    object_id = models.UUIDField(default=uuid.uuid4,
        unique=True, editable=False, verbose_name='Public identifier'
    )
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proof = models.FileField(upload_to='tenant/documents/')

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True,
        null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,blank=True,
        null=True)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.CharField(max_length=255)


