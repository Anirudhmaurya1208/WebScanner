from django.urls import path
from .views import scan_url

urlpatterns = [
    path("", scan_url, name="scan_url"),
]
