from django.shortcuts import render
from django.http import HttpResponse
from .models import Lost_Id_card

# Create your views here.


def all_ids(request):
    response = Lost_Id_card.objects.order_by('-id_number')
    return HttpResponse(response)
