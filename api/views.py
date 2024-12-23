from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import Course

@csrf_exempt
@api_view(['POST'])
def login(request):
    """Handle user login."""
    data = request.data
    user = authenticate(username=data.get('email'), password=data.get('password'))
    if user:
        return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def courses(request):
    """Get all courses."""
    courses = Course.objects.all().values('id', 'title', 'description')
    return Response(list(courses), status=status.HTTP_200_OK)
