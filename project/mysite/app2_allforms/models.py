from django.db import models


# Create a database table with an attribute for each type of form
class ModelAllFormTypes(models.Model):
    your_name = models.CharField(max_length=200, null=True)
    a_date_time_field = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.your_name

