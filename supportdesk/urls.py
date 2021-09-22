from django.urls import path
from . import views

urlpatterns = [
    path(
        "placeholder/", views.PlaceholderHome.as_view(), name="supportdesk_placeholder"
    ),
]
