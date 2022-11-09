# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


status = [("Stuck","Stuck"),("Working","Working"),("Done","Done")]
priority = [("LOW","LOW"),("MIDDLE","MIDDLE"),("HIGH","HIGH")]
current =[("NOT CURRENT","NOT CURRENT"),("CURRENT","CURRENT")]

class Project(models.Model):
    name = models.CharField(max_length=50)
    current_or_not=models.CharField(max_length=15,choices=current,default="CURRENT")
    users = models.ManyToManyField(User)
    project_status = models.CharField( max_length=10,choices=status, default="Working")
    due_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create-task")


class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=80)
    task_status = models.CharField( max_length=10,choices=status, default="Working")
    task_priority = models.CharField(max_length=10,choices=priority,default="HIGH")

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse("home")
