from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from . import forms
from .models import Hackathon, Fest, Esummit,teammatesearch
from .forms import HackForm, Festform, Esform,create_team_request


def events(request):
    data=Hackathon.objects.all()
    context = {'data': data}
    return render(request, 'events.html', context)
# Create your views here.

def hack_submit(request):
    form = forms.HackForm()
    if request.method == 'POST':
        form = HackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_model = Hackathon.objects.create(
                name=data['name'],
                image=data['image'],
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


def home(request):
    return render(request, 'test_home.html')


def teamsearch(request):
    data=teammatesearch.objects.all()
    context = {'data': data}
    # if request.method=='Post':
    #    data=request.POST
    #    value=get_object_or_404(teammatesearch, pk=pk)
    #    context = {
    #        'data': data,
    #        'value': value
    #        }
    #    redirect('team_analysis.html', context)  
  
    return render(request, 'teamsearch.html',context)

def addteamreq(request):
    if request.method == 'POST':
        form = create_team_request(request.POST)
        if form.is_valid():
            mymodel=teammatesearch.objects.create(
                hackathon_name=form.cleaned_data['hackathon_name'],
                team=form.cleaned_data['team'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                github1=form.cleaned_data['github1'],
                
                name2=form.cleaned_data['name2'],
                email2=form.cleaned_data['email2'],
                phone2=form.cleaned_data['phone2'],
                github2=form.cleaned_data['github2'],
                
                name3=form.cleaned_data['name3'],
                email3=form.cleaned_data['email3'],
                phone3=form.cleaned_data['phone3'],
                github3=form.cleaned_data['github3'],
            )
            return HttpResponse('data submitted successfully')
                
            # redirect or do something else
    else:
        form = create_team_request()
    return render(request, 'addteamreq.html',{'form': form})

def team_analysis(request,slug):
    team=teammatesearch.objects.get(slug=slug)
    context={
        'team':team,
    }
    return render(request, 'team_analysis.html',context)

