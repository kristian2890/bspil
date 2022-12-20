from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('bolig', views.bolig, name='bolig'),
    path('signin', views.signin, name='signin'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
