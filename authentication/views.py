from django.contrib.auth import views
from django.views.generic import TemplateView


class CustomLoginView(views.LoginView):
    template_name = 'registration/login.html'  # Alex you need to update this template


class CustomLogoutView(views.LogoutView):
    template_name = 'registration/logout.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
