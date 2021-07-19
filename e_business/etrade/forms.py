from etrade.models import (User, Customer)
from django.forms import ModelForm
from .models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
import logging
from django.utils.encoding import force_text


""" class CustomerForm(ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', }))

    age = forms.ModelChoiceField(queryset=Age.objects.all(), label='Age', widget=forms.Select(attrs={'class': 'form-control custom-select', }))

    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), label='Sex', widget=forms.Select(attrs={'class': 'form-control custom-select', }))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', }))

    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address', }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', }))

    marital_status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status', widget=forms.Select(attrs={'class': 'form-control custom-select', }))

    sc_handle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter Handle', }))

    edu_qualification = forms.ModelChoiceField(queryset=Education.objects.all(), label='Qualification', widget=forms.Select(attrs={'class': 'form-control custom-select', }))

    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation', }))

    state_of_origin = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State', }))

    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country', }))

    class Meta:

        model = Customer
        fields = ('first_name', 'last_name', 'email','address', 'phone_number', 'age', 'gender', 'marital_status', 'sc_handle', 'edu_qualification', 'occupation', 'state_of_origin', 'country') """


class LoginForm(ModelForm):

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password', }))

    class Meta:

        model = Customer
        fields = ('email', 'password')


class InfoForm(ModelForm):


    """ First_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', }))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', }))
    age = forms.ModelChoiceField(queryset=Age.objects.all(), label='Age', widget=forms.Select(attrs={'class': 'form-control custom-select', }))
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), label='Sex', widget=forms.Select(attrs={'class': 'form-control custom-select', }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', }))
    marital_status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status', widget=forms.Select(attrs={'class': 'form-control custom-select', }))
    sc_handle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter Handle', }))
    edu_qualification = forms.ModelChoiceField(queryset=Education.objects.all(), label='Qualification', widget=forms.Select(attrs={'class': 'form-control custom-select', }))
    occupation= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation', }))
    income = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Income', }))
    organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization', }))
    livestock = forms.ModelChoiceField(queryset=Livestock.objects.all(), label='Livestock', widget=forms.Select(attrs={'class': 'form-control custom-select', }))
    state_of_origin = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State', }))
    country=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country', }))
    
    
    age.required = False
    sc_handle.required = False
    First_name.required= True
    Last_name.required= True
  

    class Meta:

        model = MoreUserInfo
        fields = ('First_name', 'Last_name', 'gender', 'email', 'phone_number',
                  'marital_status', 'sc_handle', 'edu_qualification', 'occupation', 'income', 'organization', 'livestock', 'state_of_origin', 'country',)
  """
    pass
 
