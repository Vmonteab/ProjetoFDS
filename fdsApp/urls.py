from .views import inventory_list, checkOption
from django.urls import path


urlpatterns = [
    path("", inventory_list, name="inventory_list"),
]

