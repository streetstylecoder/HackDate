from django import forms
from .models import Hackathon, Fest, Esummit


class HackForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['name', 'venue', 'prize_money', 'description', 'date', 'Apply']
        
class Festform(forms.ModelForm):
    class Meta:
        model = Fest
        fields = ['name', 'venue', 'description', 'checkout']
        
class Esform(forms.ModelForm):
    class Meta:
        model = Esummit
        fields = ['name', 'venue', 'description', 'checkout']

