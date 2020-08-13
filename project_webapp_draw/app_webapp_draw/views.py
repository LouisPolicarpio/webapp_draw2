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

def word_prompt(request):

    if request.method == 'POST':
        form = WordPromptForm(request.POST)
        if form.is_valid():
            req_adj = Adjective.objects.order_by('?')[:form.cleaned_data['adj_amount']]
            req_verb = Verb.objects.order_by('?')[:form.cleaned_data['verb_amount']]

            context ={'form':form, 'req_adj':req_adj, 'req_verb':req_verb}
            return render(request, 'app_webapp_draw/word_prompt.html',context)

    form = WordPromptForm()
    return render(request, 'app_webapp_draw/word_prompt.html',{'form':form})

def img_prompt(request):
    return render(request,'app_webapp_draw/img_prompt.html')


@login_required(login_url='login')
def upload_img(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('myimages')
    else:
        form = UploadForm()
    context ={'form':form}
    return render(request, 'app_webapp_draw/word_prompt.html', context)


login_required(login_url='login')
def myimages(request):
    imgs = User_images.objects.filter(user=request.user).order_by('-date')
    context={"imgs":imgs}
    return render (request, 'app_webapp_draw/myimages.html',  context)
