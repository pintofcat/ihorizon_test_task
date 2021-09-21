from django.views.generic.edit import FormView
from . import forms


class RegisterView(FormView):
  template_name = "auth/register.html"
  form_class = forms.RegisterForm

class LoginView(FormView):
  template_name = "auth/login.html"
  form_class = forms.LoginForm