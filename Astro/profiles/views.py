from django.shortcuts import render, redirect
from django.http import request, HttpResponse, JsonResponse

# IMPORT DE NOS MODELS
from .models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

import profiles.forms as forms
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.shortcuts import redirect, render





class LoginPageView(View):
    template_name = 'authentication/login.html'
    # chargement du formulaire 
    form_class = forms.LoginForm 
    
    # pour recuperer le formulaire
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"    

# les methodes du tchat
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user = username, room = room_id)
    new_message.save()
    return HttpResponse("message sent !")

def getMessages(request , room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"messages" :list(messages.values())})


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/' + room +'/?username='+username) 
    
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/' + room +'/?username='+username) 


# toute les vues qui demande une authentification prealable 
# Vue principal
@login_required
def home(request):
    context =  {"users": User.objects.all()}
    return render(request, 'authentication/home.html', context)

@login_required
# LOGOUT REDIRECTION -> LOGIN
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def chat(request):
    '''on ne peut pas acceder au tchat sans etre inscrit'''
    return render(request, "chat.html")

@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)
    return render(request, 'room.html', {
        'username':username,
        'room':room,
        'room_details': room_details
    })
