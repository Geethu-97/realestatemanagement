import datetime
from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from .models import Property, Unit
# Create your views here.

def home(request):
    query = request.GET.get('search')
    properties = (
        Property.objects.filter(name__icontains=query)
        if query else Property.objects.all()
    )
    context = {'properties': properties}
    return render(request, 'home.html', context)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property_id = self.object.id
        unit_search = self.request.GET.get('unit_search', '')
        # Filter units based on the search query
        context['units'] = Unit.objects.filter(
            Q(property_id=property_id
            ) & (Q(unit_type__icontains=unit_search
            ) | Q(rent_cost__icontains=unit_search))
        )
        context['now'] = datetime.datetime.now()
        return context

