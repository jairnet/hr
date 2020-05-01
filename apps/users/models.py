from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    """Model Candidate"""
    TYPE_DOC = (
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('PA', ' Pasaporte'),
    )
    user_id = models.OneToOneField(User, on_delete=models.PROTECT)
    type_document = models.CharField(max_length=2, choices=TYPE_DOC)
    identification = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    file_cv = models.ImageField(upload_to='files/cvs')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return first_name"""
        return self.first_name
