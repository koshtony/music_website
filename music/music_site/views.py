from django.shortcuts import render

# Create your views here.


'''
    index page route
'''
def index(request):

    return render(request,'music_site/index.html')
