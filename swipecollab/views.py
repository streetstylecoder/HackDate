from django.shortcuts import render
from .models import swipeprofile,savematches

# Create your views here.

def swipecollab(request):
    return render(request, '/Users/harshdhariwal/Desktop/hackdate/simple-django-login-and-register/source/swipecollab/templates/swipecollab.html')
