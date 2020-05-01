from django.db import models
from django.contrib.auth.models import User

from apps.offers.models import Offer


class Company(models.Model):
    """Model Company"""
    user_id = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(blank=True, max_length=100)
    offer_ids = models.ManyToManyField(Offer, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return Name"""
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Companies"
