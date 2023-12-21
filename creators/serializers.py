from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Content, Creator


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['url']


class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = ['rating', 'platform', ]


class UserSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    content = ContentSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'creator', 'content']
