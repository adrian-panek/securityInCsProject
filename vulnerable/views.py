from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt

def user_info(request):
    username = request.GET.get("username", '')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT email FROM vulnerable_userprofile WHERE username = '{username}'")
        row = cursor.fetchone()

        if row:
            return HttpResponse(f"Email for {username}: {row[0]}")
        else:
            return HttpResponse("User not found")


@csrf_exempt
def update_password(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        new_password = request.POST.get("password", "")

        user = UserProfile.objects.filter(username=username).first()
        if user:
            user.password = new_password
            user.save()
            return HttpResponse("Password updated succesfully")
        else:
            return HttpResponse("User not found")
    
    return HttpResponse("Invalid request")
