from django.conf.urls import url
from sign.views import index,signup,user_profiles
from django.contrib.auth import views as auth_views

urlpatterns=[url(r"^$", index),
             url(r"home/$", index,name="home"),
             url(r'^profile/$',user_profiles,name="profile"),
             url(r"^signup/$",signup,name="sign up"),
             url(r"^signin/$", auth_views.LoginView.as_view(template_name="signin.html"),name="login"),
             url(r"^logout/$", auth_views.LogoutView.as_view(template_name="logout.html"),name="logout")]