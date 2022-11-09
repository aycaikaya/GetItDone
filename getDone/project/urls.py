from django.conf.urls import url,include
from views import ProjectsListView

urlpatterns = [url(r"^projects/$",ProjectsListView.as_view(template_name="boards.html"),name="projects")]