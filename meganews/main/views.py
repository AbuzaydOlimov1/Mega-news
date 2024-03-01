from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .serializer import *
from .models import *


@api_view(['GET'])
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, login_view, {'error_message': error_message})
    else:
        return render(request, login_view)


@api_view(['GET'])
def category(request):
    category = Category.objects.all()
    serialized_data = CategorySerializer(category, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def ad(request):
    ad = Ad.objects.all()[:3]
    serialized_data = AdSerializer(ad, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def post(request):
    post = Post.objects.all()[:4]
    serialized_data = PostSerializer(post, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def latestvideo(request):
    latestvideo = Latestvideo.objects.all()[:2]
    serialized_data = LatestvideoSerializer(latestvideo, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def handbook(request):
    handbook = Handbook.objects.last()
    serialized_data = HandbookSerializer(handbook).data
    return Response(serialized_data)


@api_view(['GET'])
def comment(request):
    comment = Comment.objects.all()[:4]
    serialized_data = CommentSerializer(comment, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def insta(request):
    insta = Insta.objects.all()[:9]
    serialized_data = InstaSerializer(insta, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def postinfo(request):
    postinfo = Postinfo.objects.last()
    serialized_data = PostinfoSerializer(postinfo).data
    return Response(serialized_data)


@api_view(['GET'])
def sendpost(request):
    sendpost = Sendpost.objects.last()
    serialized_data = SendpostSerializer(sendpost).data
    return Response(serialized_data)


@api_view(['GET'])
def sendvideo(request):
    sendvideo = Sendvideo.objects.last()
    serialized_data = SendvideoSerializer(sendvideo).data
    return Response(serialized_data)


@api_view(['GET'])
def aboutus(request):
    aboutus = AboutUs.objects.last()
    serialized_data = AboutUsSerializer(aboutus).data
    return Response(serialized_data)


@api_view(['GET'])
def team(request):
    team = Team.objects.all()[:6]
    serialized_data = TeamSerializer(team).data
    return Response(serialized_data)


@api_view(['GET'])
def contactus(request):
    contactus = Contactus.objects.last()
    serialized_data = ContactusSerializer(contactus).data
    return Response(serialized_data)

