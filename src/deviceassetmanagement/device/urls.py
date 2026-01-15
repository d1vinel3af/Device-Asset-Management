from django.urls import path
from .views import DeviceView

urlpatterns = [
    path("dashboard/", DeviceView.as_view(), name="dashboard"),
]