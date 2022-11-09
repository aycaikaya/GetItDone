from django import forms
from create.models import Task,Project
from django.contrib.auth.models import User
from django.utils.text import slugify

status = ((1,"Stuck"),(2,"Working"),(3,"Done"))
priority = ((1,"LOW"),(2,"MIDDLE"),(3,"HIGH"))
current =((0,"NOT CURRENT"),(1,"CURRENT"))

class TaskCreationForm(forms.ModelForm):
    project=forms.ModelChoiceField(queryset=Project.objects.all())
    assigned_users=forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name=forms.CharField(max_length=70)
    task_status=forms.ChoiceField(choices=status)
    task_priority=forms.ChoiceField(choices=priority)

    class Meta:
        model = Task
        fields = '__all__'

    def save(self, commit=True):
        task=super(TaskCreationForm,self).save(commit=False)
        task.project=self.cleaned_data["project"]
        task.task_name=self.cleaned_data["task_name"]
        task.task_status=self.cleaned_data["task_status"]
        task.task_priority=self.cleaned_data["task_priority"]
        task.save()
        assigned_users=self.cleaned_data["assigned_users"]
        for user in assigned_users:
            task.assign.add((user))
        if commit:
            task.save()
        return task
    def __init__(self, *args, **kwargs):
         super(TaskCreationForm, self).__init__(*args, **kwargs)
         self.fields['project'].widget.attrs['class'] = 'form-control'
         self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
         self.fields['task_name'].widget.attrs['class'] = 'form-control'
         self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
         self.fields['task_status'].widget.attrs['class'] = 'form-control'
         self.fields['task_status'].widget.attrs['placeholder'] = 'Email'
         self.fields['task_priority'].widget.attrs['class'] = 'form-control'
         self.fields['task_priority'].widget.attrs['placeholder']='Task priority'
         self.fields['assigned_users'].widget.attrs['class'] = 'form-control'
         self.fields['assigned_users'].widget.attrs['placeholder'] = 'Found date'


class ProjetCreationForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    project_status=forms.ChoiceField(choices=status)
    current_or_not=forms.ChoiceField(choices=current)
    #due_date=forms.DateField()
    description=forms.CharField(widget=forms.Textarea)
    assigned_users=forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model=Project
        fields='__all__'

    def save(self, commit=True):
        Project=super(ProjetCreationForm,self).save(commit=False)
        Project.name=self.cleaned_data["name"]
        Project.project_status=self.cleaned_data["project_status"]
        Project.current_or_not=self.cleaned_data["current_or_not"]
        Project.description=self.cleaned_data["description"]
        assigned_users=self.cleaned_data["assigned_users"]
        Project.slug = slugify(str(self.cleaned_data['name']))
        Project.save()
        for user in assigned_users:
            Project.users.add((user))
        if commit:
            Project.save()
        return Project

    def __init__(self, *args, **kwargs):
         super(ProjetCreationForm, self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs['class'] = 'form-control'
         self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
         self.fields['project_status'].widget.attrs['class'] = 'form-control'
         self.fields['project_status'].widget.attrs['placeholder'] = 'Status'
         self.fields['current_or_not'].widget.attrs['class']='form-control'
         self.fields['current_or_not'].widget.attrs['placeholder']='Is this project your current project ?'
         #self.fields['due_date'].widget.attrs['class'] = 'form-control'
         #self.fields['due_date'].widget.attrs['placeholder'] = 'Dead Line, type a date'
         self.fields['description'].widget.attrs['class'] = 'form-control'
         self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
         self.fields['assigned_users'].widget.attrs['class'] = 'form-control'

