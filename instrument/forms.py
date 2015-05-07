from django import forms
from django.contrib.auth.models import User
from instrument.models import UserProfile, numOfYear, numOfMonth, numOfDay, numOfTime


class TimeForm(forms.ModelForm):
    startHour = forms.IntegerField(help_text="Please enter the StartHour")	#Hour Time of the day from 0-23
    startMinute = forms.IntegerField(help_text="Please enter the StartMinute")	#Minute Time of the day from 0-59
    class Meta:
        # Provide an association between the ModelForm and a model
        model = numOfTime
        exclude = ('numofday',)
    def clean(self):
    	cleaned_data = self.cleaned_data
        return cleaned_data



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', )