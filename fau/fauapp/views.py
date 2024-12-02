from django.shortcuts import render
from django.http import HttpResponse


def login_custom(request):
    return render (request,'admin/login.html')