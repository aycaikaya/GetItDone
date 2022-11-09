# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from sign_forms import register_form
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "base.html")



def signup(request):
    if request.method=="POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            return redirect('/sign/signin')
    else:
        form=register_form()
    return render(request,"signup.html",{"form":form})



def noti(request):
    pass

@login_required
def user_profiles(request):
    return render(request,"user_profile.html")


def logout_view(request):
    logout(request)
    return redirect("/home")

