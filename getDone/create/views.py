# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Project_Forms import ProjetCreationForm,TaskCreationForm
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Project,Task
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateProjectView(CreateView,LoginRequiredMixin):
    model = Project
    fields = ["name","current_or_not","users","project_status","due_date","description"]

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(CreateProjectView,self).form_valid(form)


class CreateTaskView(CreateView,LoginRequiredMixin):
    model = Task
    fields = ["project","assign","task_name","task_status","task_priority"]

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(CreateTaskView,self).form_valid(form)













