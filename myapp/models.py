from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.contrib.auth.models import User

# Create your models here.
class prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this prescription')
    name = models.CharField(max_length=200, help_text='Enter patient name ')
    symptoms = models.TextField(max_length=1000, help_text='Enter  symptoms ')
    diagnosis = models.TextField(max_length=1000, help_text='Enter  diagnosis ')
    pescription = models.TextField(max_length=1000, help_text='Enter  pescription ')
    advice = models.TextField(max_length=1000, help_text='Enter  advice ')
    date=models.DateField(null=True, blank=True)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
   
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name})'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('prescription-detail', args=[str(self.id)])
