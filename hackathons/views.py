from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import forms
from .models import Hackathon, Fest, Esummit
from .forms import HackForm, Festform, Esform

# Create your views here.
def hack_submit(request):
    form = forms.HackForm()
    if request.method == 'POST':
        form = HackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_model = Hackathon.objects.create(
                name=data['name'],
                venue=data['venue'],
                prize_money=data['prize_money'],
                description=data['description'],
                date=data['date'],
                Apply=data['Apply'],
            )
            return HttpResponse('data submitted successfully')
    else:
        form = forms.HackForm()
    form = forms.HackForm()
    return render(request, 'hack_reg.html', {'form': form})

def fest_submit(request):
    
    form = forms.Festform()
    if request.method=='POST':
        form = Festform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_model = Fest.objects.create(
                name=data['name'],
                venue=data['venue'],
                description=data['description'],
                checkout=data['checkout'],
            )
            return HttpResponse('data submitted successfully')
    else:
        form=forms.Festform()
        
    return render(request, 'fest_reg.html', {'form': form})

def Es_submit(request):
    form = forms.Esform()
    if request.method=='Post':
        form = Esform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_model = Esummit.objects.create(
                name=data['name'],
                venue=data['venue'],
                description=data['description'],
                checkout=data['checkout'],
            )
            return HttpResponse('data submitted successfully')
    else:
        form=forms.Esform()
    return render(request, 'es_reg.html', {'form': form})
