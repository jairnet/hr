from django.db import models

from apps.users.models import Candidate


class Offer(models.Model):
    """Model Offer"""
    STATE_CONV = (
        ('OPEN', 'Abierta'),
        ('CLOSE', 'Cerrada'),
    )
    name = models.CharField(blank=True, max_length=100)
    date_close = models.DateTimeField()
    description = models.TextField()
    state = models.CharField(max_length=5, choices=STATE_CONV)
    date_create = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        """Return Name"""
        return self.name


class Process(models.Model):
    """Model Process"""
    STATE_ASP = (
        ('CANDIDATE', 'Aspirante'),
        ('SELECT', 'Seleccionado'),
        ('PROCESS', 'Proceso'),
        ('REJECTED', 'Rechazado'),
    )
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    state = models.CharField(max_length=12, choices=STATE_ASP)
    date_create = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        """Return state"""
        return self.state
    
    class Meta:
        ordering = ["date_create"]
        verbose_name_plural = "Process"