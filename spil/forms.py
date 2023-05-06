from django import forms
from .models import Score
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = ['priceguess', 'score', 'bidinterest']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
