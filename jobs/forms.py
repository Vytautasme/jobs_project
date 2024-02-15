from django import forms
from .models import Job, Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'company', 'expiration_date']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant_name', 'applicant_email', 'resume']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Enter your email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')