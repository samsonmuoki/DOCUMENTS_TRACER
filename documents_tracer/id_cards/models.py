from django.db import models

# Create your models here.


# class Time_Stamp_Model(models.Model):
#     created = models.DateTimeField
#     modified = models.DateTimeField

#     class Meta:
#         abstract = True


class Lost_Id_card(models.Model):
    '''
    A model for lost id_cards that are uploaded in the system
    '''
    id_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField
    sex = models.CharField(max_length=10)
    date_found = models.DateField
    place_found = models.TextField
    office_submitted = models.TextField
    picture = models.FileField

    def __str__(self):
        return self.id_number


class Searched_id_card(models.Model):
    '''
    A model for lost id cards that have been searched for in the system
    '''
    id_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=50)
    contact_numder = models.CharField(max_length=15)
    contact_email = models.EmailField

    def __str__(self):
        return self.id_number
