from django.views.generic import DetailView, ListView
from .models import Destinations


class IndexView(ListView):
    template_name = 'destinations/index.html'
    context_object_name = 'latest_destination_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Destinations.objects.order_by('-name')[:5]


class DestinationDetailView(DetailView):
    model = Destinations
    template_name = 'destinations/detail.html'
