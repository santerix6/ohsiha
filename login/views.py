from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from.models import TestTaulu
import requests

# Create your views here.
post =[
    {
        'nimi' : 'Santeri',
        'paikkakunta' : 'Tampere',
        'tauti' : 'korona'
    }
]
api_address = "https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData"
def home (request):
    context = {
        'post' :post
    }
    return render(request, 'login/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})

@login_required
def profile_edit(request):
    return render(request, 'login/editprofile.html')

@login_required
def lisaa(request):
    if request.method == 'GET':
        return render(request, 'login/lisaa.html')
    if request.method =="POST":
        taulu = TestTaulu()
        taulu.pva = request.POST.get("pva")
        taulu.sairaanhoitopiiri = request.POST.get("dis")
        taulu.alkuperamaa = request.POST.get("src")
        taulu.alkupera = request.POST.get("infsrc")
        taulu.lisaaja = request.user
        taulu.save()
        return redirect("login-home")
    # testi = TestTaulu()
    # testi.col = 'nicenice'
    # testi.save()
@login_required
def listaa(request):
    taulu = TestTaulu.objects.all().values()
    print(taulu)
    taulu = {
        'taulu' : taulu
    }
    return render(request, 'login/listaa.html', taulu)
@login_required
def api(request):
    data = requests.get(api_address).json()
    taulu = TestTaulu()
    taulu.pva = data['confirmed'][0]['date']
    taulu.sairaanhoitopiiri = data['confirmed'][0]['healthCareDistrict']
    taulu.alkupera = data['confirmed'][0]['infectionSource']
    taulu.alkuperamaa = data['confirmed'][0]['infectionSourceCountry']
    taulu.lisaaja = request.user
    taulu.save()
    for x in data['confirmed']:
        print('id: ',x['id'])
        print('date: ',x['date'])
        print('HCD: ',x['healthCareDistrict'])
        print('infectionSource: ', x['infectionSource'])
        print('infectionSourceCountry: ',x['infectionSourceCountry'])
