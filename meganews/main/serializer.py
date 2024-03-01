from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LatestvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latestvideo
        fields = "__all__"


class HandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbook
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class InstaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insta
        fields = "__all__"


class PostinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postinfo
        fields = "__all__"


class SendpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendpost
        fields = "__all__"


class SendvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendvideo
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = "__all__"

