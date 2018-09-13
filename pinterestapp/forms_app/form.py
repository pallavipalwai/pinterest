from django import forms
from django.forms import ModelForm

from pinterestapp.models import Pin


class SignUp(forms.Form):

    username = forms.CharField(
        required=True,
        max_length=100,
        label="UserName",
    )

    password=forms.CharField(
        required=True,
        max_length=100,
        label="Password"
    )


class Login_form(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        label="UserName"
    )

    password = forms.CharField(
        required=True,
        max_length=100,
        label="Password"
    )



class Pin_form(forms.ModelForm):
    class Meta:
        model=Pin
        exclude=['id']
        fields=['title','photo','website']