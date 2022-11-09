from django.conf.urls import url
from create.views import CreateProjectView,CreateTaskView

urlpatterns=[url(r"^project/$",CreateProjectView.as_view(template_name="project_form.html"),name="create-project"),
            url(r"^task/$", CreateTaskView.as_view(template_name="task_form.html"),name="create-task")
            ]