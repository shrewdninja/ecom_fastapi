from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Feedback
from .validations import validate_description,validate_email,validate_username, validate_name

INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl border'

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Enter username',
         'class': 'w-full py-4 px-6 rounded-xl'
    }), validators=[validate_username])
    password=forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Enter password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))

class CustomChangePasswordForm(PasswordChangeForm):
     old_password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Enter old password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))
     new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Enter new password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))
     new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Confirm new password',
         'class': 'w-full py-4 px-6 rounded-xl'
    }))
     class meta:
        model = User

class SignupForm(UserCreationForm):
     class Meta:
         model=User
         fields=('username', 'email', 'password1', 'password2')
     username=forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Username',
          'class': 'w-full py-4 px-6 rounded-xl'
     }), validators=[validate_username])
     email=forms.CharField(widget=forms.EmailInput(attrs={
         'placeholder': 'Email address',
         'class': 'w-full py-4 px-6 rounded-xl'
     }), validators=[validate_email])
     password1=forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Password',
         'class': 'w-full py-4 px-6 rounded-xl'
     }))
     password2=forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder': 'Re-enter Password',
         'class': 'w-full py-4 px-6 rounded-xl'
     }))

class FeedbackForm(forms.ModelForm):
     class Meta:
          model=Feedback
          fields=('first_name', 'last_name', 'email', 'description', 'image')
          first_name=forms.CharField(widget=forms.TextInput(attrs={
               'placeholder': 'First Name',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_name])
          last_name=forms.CharField(widget=forms.TextInput(attrs={
               'placeholder': 'First Name',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_name])
          email=forms.CharField(widget=forms.EmailInput(attrs={
               'placeholder': 'Email address',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_email])
          description=forms.CharField(widget=forms.TextInput(attrs={
               'placeholder': 'Enter details here',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_description])
          image=forms.FileInput(attrs={
               'class': 'w-full px-6 py-4 rounded-xl border'
          })