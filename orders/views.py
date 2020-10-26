from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


def home_view(request, *args, **kwargs):
    return render(request, "detail_view/home.html")
