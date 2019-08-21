from django.shortcuts import render
from django.http import HttpResponse
from .models import Lost_Id_card

# Create your views here.


def home(request):
    return render(request, 'id_cards/home.html')


def all_ids(request):
    response = Lost_Id_card.objects.order_by('-id_number')
    return HttpResponse(response)


def report_id(request):
    return render(request, 'id_cards/report_id.html')


def id_detail(request, id_number):
    try:
        id_card = Lost_Id_card.objects.get(pk=id_number)
    except Lost_Id_card.DoesNotExist:
        return render(request, 'polls/nocard.html')
        # send_mail()
    return render(request, 'polls/detail.html', {'id': id_card})
