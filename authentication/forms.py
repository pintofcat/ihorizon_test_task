from django import forms

class RegisterForm(forms.Form):
  username = forms.CharField(label='Your username', max_length=100)
  password = forms.CharField(
    label='Your password', 
    max_length=100, 
    widget=forms.PasswordInput()
  )
  is_agent = forms.BooleanField()

class LoginForm(forms.Form):
  username = forms.CharField(label='Your username', max_length=100)
  password = forms.CharField(
    label='Your password', 
    max_length=100, 
    widget=forms.PasswordInput()
  )