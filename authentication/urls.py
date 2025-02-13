from .views import RegisterationView,UsernameValidationView, EmailValidationView, VerficationView, LoginView, LogoutView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('register', RegisterationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name='validate-username'),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name='validate-email'),
    path('activate/<uid>/<token>', VerficationView.as_view(),name='activate'),
]
