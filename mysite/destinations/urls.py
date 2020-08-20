from django.urls import path
from . import views

urlpatterns = [
    # ex: /destinations/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /destinations/5/
    path('destinations/<int:pk>/', views.DestinationDetailView.as_view(), name='detail'),
]
