from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Home,Events,About,EventCategory,Contacts,Items,Concerts,Blog,Comments
from .youtube_api import get_youtube_videos
import json

# Create your views here.
'''
   user management
'''

def register_page(request):
    
    
    return render(request,'music_site/register_page.html')

def register(request):
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    
    print(password)
    
    msg = ""
    
    if password == password2:
        
        if User.objects.filter(username=username).exists():
            
            msg += "<strong style='color:red'>username already exists </strong>"
            
        elif User.objects.filter(email=email).exists():
            
            msg+= "<strong style='color:red'>username already exists </strong>"
        
        else:
            
            user = User(
            username=username,
            email=email,
            password=password
            )

            user.save()
            
            msg+= "<strong style='color:green'>user created successfully </strong>"
            
    else:
        
        msg+= "<strong style='color:red'>Password does not match </strong>"
        
        
    return HttpResponse(msg)


def login_page(request):
    
    
    username = request.POST.get('username')
    password = request.POST.get('password') 
    
    user = authenticate(username=username,password=password)
    
    msg = ''
    if user is not None:
            
            if user.is_active:
                
                login(request,user)
                msg+='<strong color="green"> Login successfull, Login status updated</strong>'
                
                
                
            else:
                
                msg += '<strong color="red"> This user is Inactive contact admin </strong>' 
    else:
            
            msg+='<strong style="color:red"> Invlaid username or password </strong>'  
        
    return HttpResponse(msg)
    
    
        
        
            
            
    


    
    


'''
    index page route
'''
def index(request):
    
    latest = get_youtube_videos()[-2]
  
    
    details = Home.objects.all()
    events = Events.objects.all().order_by('dates')[:5]
    events_category = EventCategory.objects.all()
    
    if len(Concerts.objects.all())>0:
        
        concert=Concerts.objects.latest('-pk')
    
        
    else:
        
        concert=Concerts.objects.all()
    
    contact = Contacts.objects.all()[0]
  
    contxt = {"detail":details[0], "events":events, "events_category":events_category,"latest":latest,"concert":concert,"contact":contact}

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
    
    contact = Contacts.objects.all()[0]
    
    contxt = {'about':abouts,"events_category":events_category,"contact":contact}
    
    return render(request,'music_site/about.html',contxt)

def youtube_videos(request):
    
    latest = get_youtube_videos()[-2]
    
    contact = Contacts.objects.all()[0]
    
  
    contxt = {"videos":get_youtube_videos(),"latest":latest,"contact":contact}	
    
    return render(request,'music_site/youtube_videos.html',contxt)


def concerts_page(request):
    
    concerts = Concerts.objects.all()
    
    contxt = {"concerts":concerts}
    
    return render(request,'music_site/concerts.html',contxt)
    

def blog_page(request):
    
    if len(Blog.objects.all())>0:
        
        latest = Blog.objects.latest('pk')
    
    else:
        
        latest = Blog.objects.all()
        
    blog_list = Blog.objects.all().order_by('-pk')
    
    page = request.GET.get('page',1)
    
    paginator = Paginator(blog_list,6)
    
    try:
        blogs = paginator.get_page(page)
        
    except PageNotAnInteger:
        
        blogs = paginator.page(1)
        
    except EmptyPage:
        
        blogs = paginator.page(paginator.num_pages)
    
    contact = Contacts.objects.all()[0]
    
    contxt = {"blogs":blogs,"latest":latest,"contact":contact}
    
    return render(request,'music_site/blog.html',contxt)


def blog_details(request,pk):
    
    blog = Blog.objects.get(pk=pk)
    
    comments = Comments.objects.filter(blog=blog).order_by('-pk')
    
    contact = Contacts.objects.all()[0]
    
    
    if len(Blog.objects.all())>2:
        
        latest = Blog.objects.all().order('-pk')[:2]
        
    else:
        
        latest = Blog.objects.all()
    
    contxt = {"blog":blog,"latest":latest,"contact":contact,"comments":comments}	
    
    return render(request,'music_site/blog_details.html',contxt)


def add_comments(request,pk):
    
    comment = request.POST.get("comment")
    blog = Blog.objects.get(pk=pk)
    
    comment = Comments(
        comment = comment,
        blog=blog,
        sent_by = request.user,
        category = "public"
        
    )
    
    comment.save()
    
    comments = Comments.objects.all().order_by('-pk')
    
    contxt = {"comments":comments}
    
    
    
    return render(request,'music_site/comments.html',contxt)

def add_reply(request,pk):
    
    pass
        

def contacts_page(request):
    
    if len(Contacts.objects.all())>0:
        
        contacts = Contacts.objects.all()[0]
        
    else:
        contacts = Contacts.objects.all()
        
    contxt = {"contact":contacts}
        
    return render(request,'music_site/contacts.html',contxt)

def store_page(request):
    
    item_list = Items.objects.all()
    
    page = request.GET.get('page',1)
    
    paginator = Paginator(item_list, 6)
    
    try:
        
        items = paginator.get_page(page)
        
    except PageNotAnInteger:
        
        items = paginator.page(1)
        
    except EmptyPage:
        
        items = paginator.page(paginator.num_pages)
        
    
    
    
    
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