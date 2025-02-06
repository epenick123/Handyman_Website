# myapp/urls.py

from django.urls import path
from .views import home  # Import your view

urlpatterns = [
    path('', home, name='home'),  # Maps the root URL to the home view
]