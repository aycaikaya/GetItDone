# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from create.models import Project,Task
from sign.models import User_Profile
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,UpdateView
from django.shortcuts import render

class ProjectsListView(ListView):
    model = Project
    template_name = "boards.html"
    context_object_name = "boards"
    ordering = ["-due_date"]

class ProjectsDetailView(DetailView):
    model = Project




class TasksListView(ListView):
    model = Task

    context_object_name = "tasks"

