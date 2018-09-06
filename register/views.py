from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Doner
from .forms import RegisterForm

def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        doner= form.save(commit=False)
        user= form.cleaned_data.get('doner')
        doner.doner=user
        doner.blood_group = form.cleaned_data.get('blood_group')
        doner.mobile_no = form.cleaned_data.get('mobile_no')
        doner.email = form.cleaned_data.get('email')
        doner.city = form.cleaned_data.get('city')

        doner.save()
        return render(request, 'thanks0.html', {'doner': doner,'user':user})
    context = {
            "form": form,
        }
    return render(request, 'register.html', context)
