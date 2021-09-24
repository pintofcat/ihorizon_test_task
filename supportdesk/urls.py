from django.urls import path

from . import views

urlpatterns = [
    path("tickets/new", views.create_ticket, name="create_ticket"),
    path("tickets/", views.list_tickets, name="list_tickets"),
    path("tickets/<int:ticket_id>", views.get_ticket, name="detail_tickets"),
    path("tickets/<int:ticket_id>/update", views.update_ticket, name="update_ticket"),
]
