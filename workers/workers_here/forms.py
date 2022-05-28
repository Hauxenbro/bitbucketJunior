from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Workers

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput)
    username = forms.CharField(label='Имя', widget=forms.TextInput)
    password1 = forms.CharField(label='Пароль', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ('name', 'photo', 'working_place', 'salary', 'parent')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'working_place': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'parent': forms.Select(attrs={'class':'form-control'}),
        }