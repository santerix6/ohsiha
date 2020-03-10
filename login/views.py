from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
post =[
    {
        'nimi' : 'Santeri',
        'paikkakunta' : 'Tampere',
        'tauti' : 'korona'
    }
]
def home (request):
    context = {
        'post' :post
    }
    return render(request, 'login/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login-home')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})
