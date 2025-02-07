from django.shortcuts import render

class Member:
    def __init__(self, name, age, gender, dupr):
        self.name = name
        self.age = age
        self.gender = gender
        self.dupr = dupr

# Create a list of Cat instances
members = [
    Member('Judy Bloom', 42, 'female', 3.0),
    Member('Hank Wilson', 35, 'male', 2.5),
    Member('Tony Smith', 55, 'male', 4.0),
    Member('Gladys Goldberg', 27, 'female', 3.5)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def member_index(request):
    return render(request, 'members/index.html', {'members': members})
