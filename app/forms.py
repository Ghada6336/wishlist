from django import forms
from django.contrib.auth.models import User
from .models import Item ,NewItem

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name','password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class CreateForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['owner']

class ItemForm(forms.ModelForm):
    class Meta:
        model = NewItem
        exclude = ['new']
