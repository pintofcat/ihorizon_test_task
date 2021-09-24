from enum import Enum

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

COMPLETED = "COMPLETED"
IN_PROGRESS = "IN_PROGRESS"


STATUSES = (
    (COMPLETED, "completed"),
    (IN_PROGRESS, "in_progress"),
)


class Ticket(models.Model):
    """Ticket model."""

    summary = models.CharField(max_length=255)
    description = models.TextField()
    high_priority = models.BooleanField(default=False)
    status = models.CharField(choices=STATUSES, max_length=12, default=IN_PROGRESS)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
