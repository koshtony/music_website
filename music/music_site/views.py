from django.shortcuts import render
from .models import Home

# Create your views here.


'''
    index page route
'''
def index(request):
    
    details = Home.objects.all()
    
    contxt = {"detail":details[0]}

    return render(request,'music_site/index.html',contxt)
