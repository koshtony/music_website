from django.shortcuts import render
from django.http import JsonResponse
from .models import Home,Events,About,EventCategory,Contacts,Items
from .youtube_api import get_youtube_videos
import json

# Create your views here.


'''
    index page route
'''
def index(request):
    
    latest = get_youtube_videos()[-2]
    details = Home.objects.all()
    events = Events.objects.all().order_by('dates')[:5]
    events_category = EventCategory.objects.all()
    
    
    
    contxt = {"detail":details[0], "events":events, "events_category":events_category,"latest":latest}

    return render(request,'music_site/index.html',contxt)



'''
    about page route

'''
def about(request):
    
    if len(About.objects.all())>0:
        abouts = About.objects.all()[0]
    
    else:
        
        abouts = About.objects.all()
    
    events_category = EventCategory.objects.all()
    
    contxt = {'about':abouts,"events_category":events_category}
    
    return render(request,'music_site/about.html',contxt)

def youtube_videos(request):
    
    latest = get_youtube_videos()[-2]
    
    print(get_youtube_videos())
    contxt = {"videos":get_youtube_videos(),"latest":latest}
    
    return render(request,'music_site/youtube_videos.html',contxt)

def contacts_page(request):
    
    if len(Contacts.objects.all())>0:
        
        contacts = Contacts.objects.all()[0]
        
    else:
        contacts = Contacts.objects.all()
        
    contxt = {"contact":contacts}
        
    return render(request,'music_site/contacts.html',contxt)

def store_page(request):
    
    items = Items.objects.all()
    
    contxt = {"items":items}
    
    return render(request,'music_site/store.html',contxt)
    
    
    
    

def get_contacts(request):
    
    if len(Contacts.objects.all())>0:
        
        contact = {
            "name":Contacts.objects.all()[0].name,
            "phone":Contacts.objects.all()[0].phone,
            "email":Contacts.objects.all()[0].email,
            "address":Contacts.objects.all()[0].address,
            "facebook_link":Contacts.objects.all()[0].facebook_link,
            "insta_link":Contacts.objects.all()[0].insta_link,
            "youtube_link":Contacts.objects.all()[0].youtube_link,
            "location_link":Contacts.objects.all()[0].location_link,	
            
        }
        
    else:
        
        contact = {
            "name":"",
            "phone": "",
            "email": "",
            "address": "",
            "facebook_link": "",
            "insta_link": "",
            "youtube_link": "",
            "location_link": "",    
            
        }
    
    contact = json.dumps(contact)
    return JsonResponse(contact,safe=False)