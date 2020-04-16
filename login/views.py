from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from.models import TestTaulu, KuolemaTaulu
import requests
import datetime

# Create your views here.
post =[
    {
        'nimi' : 'Santeri',
        'paikkakunta' : 'Tampere',
        'tauti' : 'korona'
    }
]
api_address = "https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData/v2"
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
def listaa_tapaukset(request):
    taulu = TestTaulu.objects.all().values()
    taulu = {
        'taulu' : taulu
    }
    return render(request, 'login/listaa.html', taulu)
@login_required
def listaa_kuolemat(request):
    kuolemat = KuolemaTaulu.objects.all().values()
    kuolemat = {
        'kuolemat': kuolemat
    }
    return render(request, 'login/kuolemat.html', kuolemat)
@login_required
def api(request):
    data = requests.get(api_address).json()
    TestTaulu.objects.all().delete()


    taulu = TestTaulu()
    ktaulu = KuolemaTaulu()
    for y in data['deaths']:
        ktaulu.kuolemaid = y['id']
        a = y['date'].split('T')
        b = a[0]
        ktaulu.pva = b
        ktaulu.sairaanhoitopiiri = y['healthCareDistrict']
        ktaulu.save()
    for x in data['confirmed']:
        ktaulu.kuolemaid = y['id']
        a = x['date'].split('T')
        b = a[0]
        taulu.pva = b
        taulu.sairaanhoitopiiri = x['healthCareDistrict']
        taulu.potilasid = x['id']
        taulu.alkupera = x['infectionSource']
        taulu.alkuperamaa = x['infectionSourceCountry']
        taulu.lisaaja = request.user
        taulu.save()
    messages.success(request, f'Data päivitetty!')
    return redirect("login-home")
@login_required
def visualisoi(request):
    day_delta = datetime.timedelta(days=1)
    end_date = datetime.date.today()
    start_date = datetime.date(2020,1,29)
    keissi_maarat = []
    for i in range((end_date - start_date).days):
        date = start_date + i*day_delta
        kaset = TestTaulu.objects.filter(pva=date).count()
        strdate = date.strftime("%m/%d/%Y")
        case = {
            'paiva' : strdate,
            'lkm' : kaset
        }
        keissi_maarat.append(case)
    data =  keissi_maarat
    print(data)
    return render(request, "login/visual.html", {'data': data})
