from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from .models import *

class CreatUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #clean data
    def save(self, commit=True):
        user = super(CreatUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class WordPromptForm(forms.Form):
    adj_amount = forms.IntegerField()

    verb_amount = forms.IntegerField()
