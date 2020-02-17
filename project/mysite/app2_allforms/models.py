from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create a database table with an attribute for each type of form
class ModelAllFormTypes(models.Model):
    your_name = models.CharField(max_length=200, null=True)
    a_date_time_field = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.your_name

    #def get_absolute_url(self):
    #    return reverse('app2_allforms.everything-detail', kwargs={'pk': self.pk})

    #def get_fields(self):
    #    return {
    #        #"your_name": self.your_name,
    #        "your_name": 'lala',
    #        "your_name2": 'lala2',
    #        #"a_date_time": a_date_time_field,
    #        }

