from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Receiver
from .forms import ReceiverForm
from register.models import Doner
import requests

url = "https://www.fast2sms.com/dev/bulk"

def NeedBloodView(request):
    form = ReceiverForm(request.POST or None)
    if form.is_valid():
        receiver= form.save(commit=False)
        user= form.cleaned_data.get('receiver')
        receiver.receiver=user
        blood_group=form.cleaned_data.get('blood_group')
        print(blood_group)
        receiver.blood_group = blood_group
        mobile_no=form.cleaned_data.get('mobile_no')
        receiver.mobile_no = mobile_no
        receiver.email = form.cleaned_data.get('email')
        hospital=form.cleaned_data.get('hospital')
        receiver.hospital = hospital
        receiver_city=form.cleaned_data.get('city')
        receiver.city = receiver_city

        receiver.save()
        numbers=[]
        for doner in Doner.objects.filter(city__startswith=receiver_city):
            numbers.append(doner.mobile_no)

        msg= user +" Need "+ blood_group  + "Blood At "+ hospital+","+ receiver_city +" Call on "+mobile_no+" from Helping Hand."
        for number in numbers:

            payload = "sender_id=FSTSMS&message="+msg+"&language=english&route=p&numbers="+number
            headers = {
            'authorization': "Xn4BP6YkCtab0iTuSgH8WEzJONveKUpIhwARlDx3MZroqFcmVQcD8kBNCzfen2FPpIlsHtZKmJ47X9gi",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)

        return render(request, 'thanks1.html', {'receiver': receiver,'user':user})
    context = {
            "form": form,
        }
    return render(request, 'need.html', context)
