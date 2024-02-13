import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class RandomNumberGenerator:
    def __init__(self):
        self.counter = 0

    def generate_number(self):
        self.counter += 1
        if random.random() < 0.1:  # Pravděpodobnost, že padne 0 je 10%
            return 0
        else:
            return random.randint(1, 10)

generator = RandomNumberGenerator()

def models_list(request):
    random_number = generator.generate_number()
    return HttpResponse(f"Random number: {random_number}")
