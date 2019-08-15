from django.db import models

# Create your models here.


class Lost_ID_card(models.model):
    """
    Model for lost national ids that will be uploaded
    """
    id_number = models.CharField(maxlength=15)
    full_name = models.CharField(maxlength=15)
    date_of_birth = models.DateField
    sex = models.CharField(maxlength=15)
    date_found = models.DateTimeField('Less than or equal to Today')
    place_found = models.TextField
    office_submitted = models.TextField
    picture = models.FileField


class Searched_id(models.model):
    """
    Model for searched ids
    """
    id_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=50)
    contact_number = models.CharField(maxlength=15)
    contact_email = models.EmailField
