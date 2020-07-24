from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.

from .models import *
from .forms import *

#@login_required(login_url='login')
def home(request):
    return render(request,'app_webapp_draw/index.html')

def loginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "inccorect username or password")

    return render(request,'app_webapp_draw/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreatUserForm()

        if request.method =="POST":
            form = CreatUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'account ' +user+ ' has been made')
                return redirect(loginPage)
        context = {'form' : form}
        return render(request,'app_webapp_draw/register.html', context)

class word_prompt(TemplateView):
    template_name = 'app_webapp_draw/word_prompt'

    def get(self,request):
        form = WordPromptForm()
        return render(request, self.template_name, {'form':form})



login_required(login_url='login')
def myimages(request):
    imgs = User_images.objects.filter(user=request.user)
    context={"imgs":imgs}
    return render (request, 'app_webapp_draw/myimages.html',  context)
