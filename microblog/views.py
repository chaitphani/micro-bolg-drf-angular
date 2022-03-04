from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request, path=''):
    return render(request, 'index.html')


class UserApiview(APIView):

    serializer_class = UserCreateSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostApiView(APIView):

    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)