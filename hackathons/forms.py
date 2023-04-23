from django import forms
from .models import Hackathon, Fest, Esummit,teammatesearch


class HackForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['name','image', 'venue', 'prize_money', 'description', 'date', 'Apply']
        
class Festform(forms.ModelForm):
    class Meta:
        model = Fest
        fields = ['name', 'venue', 'description', 'checkout']
        
class Esform(forms.ModelForm):
    class Meta:
        model = Esummit
        fields = ['name', 'venue', 'description', 'checkout']
        
class create_team_request(forms.ModelForm):
    class Meta:
        model = teammatesearch
        fields=['hackathon_name','team','name','email','phone','github1','name2','email2','phone2','github2','name3','email3','phone3','github3','developer_role_required','preffered_languages']


class team_filter(forms.Form):
    DEVELOPER_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mern', 'MERN Stack'),
    )
    LANGUAGE_CHOICES = (
        ('react', 'React.js'),
        ('next', 'Next.js'),
    )

    developer_role_required = forms.ChoiceField(choices=DEVELOPER_CHOICES)
    preffered_languages = forms.ChoiceField(choices=LANGUAGE_CHOICES)