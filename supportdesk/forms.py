from django import forms

from supportdesk.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("summary", "description", "high_priority", "high_priority")
