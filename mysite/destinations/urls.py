from django.urls import path
from .views import DestinationsView

urlpatterns = [
    path('', DestinationsView.as_view(template_name='destinations.html'), name='destinations'),
]
