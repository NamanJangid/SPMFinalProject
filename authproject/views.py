from django.contrib.auth import authenticate, login

from django.shortcuts import render
from pyexpat.errors import messages

import manage

uname = ''


# Create your views here.
def login_request(requests):
    # form = render(request,'Login.html')

    return render(requests, 'Login.html', {"username": manage.username})


def main_request(request):
    username = request.POST(request.user)
    accessToken = manage.accessToken
    # if request.method == 'POST':
    #     manage.accessToken = request.POST['AccessToken']
    #     accesstoken = request.POST['AccessToken']
    return render(request, 'main.html', {"name": manage.username, "AccessToken": accessToken})


def repos(request):
    accessToken = manage.accessToken
    return render(request, 'Repos.html', {"AccessToken": accessToken})
