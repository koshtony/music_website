from django.urls import path 
from . import views 
from .views import index,about,youtube_videos,get_contacts,contacts_page,\
    store_page,concerts_page,blog_page,blog_details,add_comments,register_page,login_page,register

urlpatterns = [

    path('',views.index,name="site-index"),
    path('about',views.about,name="site-about"),
    path('youtube-videos',views.youtube_videos,name="site-youtube-videos"),
    path('get_contacts',views.get_contacts,name="site-get-contacts"),
    path('contacts_page',views.contacts_page,name="site-contact-page"),
    path('store_page',views.store_page,name="site-store-page"),
    path('concerts_page',views.concerts_page,name="site-concert-page"),
    path('blog_page',views.blog_page,name="site-blog-page"),
    path('blog_details/<int:pk>',views.blog_details,name="site-blog-details"),
    path('add_comments/<int:pk>',views.add_comments,name="site-add-comments"),
    path('register_page/',views.register_page,name="site-register-page"),
    path('register/',views.register,name="site-register"),
    path('login_page/',views.login_page,name="site-login-page"),
         
    
]