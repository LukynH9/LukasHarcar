import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def models_list(reguest):
    random_number = random.randint(a 1, b 100)
    return HttpResponse(f"Random number"  )
