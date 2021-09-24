from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from supportdesk.forms import TicketForm
from supportdesk.models import COMPLETED, Ticket


class PlaceholderHome(TemplateView):
    template_name = "supportdesk/placeholder.html"


def create_ticket(request):
    user = request.user
    form = TicketForm()
    user_group = (
        request.user.groups.first().name
    )  # test run, every user has only 1 group
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.instance.creator = user
            form.save()
            return redirect(reverse_lazy("list_tickets"))

    return render(
        request, "supportdesk/create_ticket.html", {"form": form, "group": user_group}
    )


def update_ticket(request, ticket_id):
    data = request.POST
    if data.get("to_complete") == "Mark as completed":
        Ticket.objects.filter(id=ticket_id).update(status=COMPLETED)
    return redirect(reverse_lazy("list_tickets"))


def list_tickets(request):
    tickets = Ticket.objects.all().order_by("-id")
    user = request.user
    user_group = user.groups.first().name  # test run, every user has only 1 group
    if user_group == "customer":
        tickets = tickets.filter(creator=user)
    return render(
        request,
        "supportdesk/list_tickets.html",
        {"tickets": tickets, "group": user_group},
    )


def get_ticket(request, ticket_id: int):
    user_group = (
        request.user.groups.first().name
    )  # test run, every user has only 1 group
    ticket = Ticket.objects.filter(id=ticket_id)
    return render(
        request,
        "supportdesk/list_tickets.html",
        {"tickets": ticket, "group": user_group},
    )
