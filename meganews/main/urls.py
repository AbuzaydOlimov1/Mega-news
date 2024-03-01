from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', category),
    path('ad/', ad),
    path('post/', post),
    path('latestvideo/', latestvideo),
    path('handbook/', handbook),
    path('comment/', comment),
    path('insta/', insta),
    path('login/', login_view),
    path('postinfo/', postinfo),
    path('sendpost/', sendpost),
    path('sendvideo/', sendvideo),
    path('aboutUs/', aboutus),
    path('team/', team),
    path('contactus/', contactus),
]