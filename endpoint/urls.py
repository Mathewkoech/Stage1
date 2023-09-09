from django.urls import path
from .views import EndpointView

urlpatterns = [
  path('endpoint/', EndpointView.as_view(), name='endpoint'),
]