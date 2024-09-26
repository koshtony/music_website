from django.shortcuts import render
from .models import Home,Events,About,EventCategory

# Create your views here.


'''
    index page route
'''
def index(request):
    
    details = Home.objects.all()
    events = Events.objects.all().order_by('dates')[:5]
    events_category = EventCategory.objects.all()
    
    contxt = {"detail":details[0], "events":events, "events_category":events_category}

    return render(request,'music_site/index.html',contxt)
