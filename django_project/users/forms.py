from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import UserProfile

matriculas = ["20192085010232","20192085010231","20192085010321"]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['matricula']
        
    def clean_matricula(self):
        lista = matriculas
        matricula = self.cleaned_data['matricula']
        if matricula not in matriculas:
            raise ValidationError('Matrícula não cadastrada.')
        return matricula

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
