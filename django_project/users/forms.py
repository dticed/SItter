from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

matriculas = ["20192085010232","20192085010231"]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    matricula = forms.CharField(max_length=14, required=True)

    class Meta:
        model = User
        fields = ['username', 'email','matricula', 'password1', 'password2']

    def clean_matricula(self):
        lista = matriculas
        matricula = self.cleaned_data['matricula']
        if matricula not in matriculas:
            raise ValidationError('Matrícula não cadastrada.')
        return matricula

        
