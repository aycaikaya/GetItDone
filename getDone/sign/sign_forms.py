from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register_form(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    bio=forms.CharField(max_length=150,widget=forms.Textarea)

    class Meta:
        model = User
        fields=['username','first_name','last_name','bio','email','password1','password2']