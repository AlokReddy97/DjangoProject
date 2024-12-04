from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt

def hello_world(request):
    return HttpResponse("Hello, world!")

from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email is unique
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please use a different email.")
            return redirect('signup')

        # Create a new user
        UserDetails.objects.create(username=username, email=email, password=password)
        messages.success(request, "Signup successful! Please login.")
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('success')
        except UserDetails.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

def get_all_users(request):
    users = UserDetails.objects.all()
    return render(request, 'all_users.html', {'users': users})

def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return render(request, 'user_detail.html', {'user': user})
    except UserDetails.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('get_all_users')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Loginify.models import UserDetails
from Loginify.serializers import UserDetailsSerializer

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Loginify.models import UserDetails
from Loginify.serializers import UserDetailsSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserDetails
from .serializers import UserDetailsSerializer

@csrf_exempt
def update_user(request, email):
    try:
        # Check if a user with the given email exists
        user = UserDetails.objects.get(email=email)

        if request.method == 'POST':
            # Parse the incoming JSON data
            data = JSONParser().parse(request)

            # Update only the fields provided in the request
            serializer = UserDetailsSerializer(user, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()  # Save the updated user details
                return JsonResponse({'message': 'User details updated successfully'}, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)

        else:
            return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=405)

    except UserDetails.DoesNotExist:
        # Return error if no user is found with the given email
        return JsonResponse({'error': 'User not found: Email does not exist.'}, status=404)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Loginify.models import UserDetails  # Import your model

@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':  # Check if the request is a DELETE request
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully.'}, status=200)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method. Use DELETE.'}, status=405)
