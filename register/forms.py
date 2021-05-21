import datetime
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Booking

from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserBookingForm(forms.ModelForm):	
	Advisor = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	date = forms.DateField()
	time = forms.TimeField()
	class Meta:
		model = Booking
		fields = ['Advisor', 'username', 'date', 'time']
        
        # Check if a date is not in the past.
        