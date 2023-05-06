from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('bolig', views.bolig, name='bolig'),
    #path('signin', views.signin, name='signin'),
    #path("signup/", SignUpView.as_view(), name="signup"),
    #path("logout", views.logout_request, name= "logout"),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('register', views.register_page, name='register'),
    path('bolig404', views.bolig404, name='bolig404'),
    path('post_bud', views.post_bud, name='post_bud'),
    path('highscore', views.highscore, name='highscore')
]
