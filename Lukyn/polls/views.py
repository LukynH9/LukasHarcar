import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def models_list(request):
    from django.http import HttpResponse
    import random

    class RandomNumberGenerator:
        def __init__(self):
            self.counter = 0

        def generate_number(self):
            self.counter += 1
            if self.counter % 5 == 0:
                return 0
            else:
                return random.randint(1, 1000)

    generator = RandomNumberGenerator()

    def get_random_number():
        random_number = generator.generate_number()
        return random_number

    gamble = random_result = get_random_number()
    print(f"Random number: {random_result}")
    return render(request,'polls/polls.html', {"random_number": gamble})
