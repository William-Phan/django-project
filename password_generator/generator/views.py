import string
import random
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = string.ascii_lowercase
    length = int(request.GET.get('length'))
    have_uppercase = request.GET.get('uppercase')
    have_digit = request.GET.get('digit')
    have_special_characters = request.GET.get('character')

    if have_uppercase:
        characters += string.ascii_uppercase
    if have_digit:
        characters += string.digits
    if have_special_characters:
        characters += string.punctuation

    generated_password = [random.choice(characters) for _ in range(length)]
    random.shuffle(generated_password)
    generated_password = ''.join(generated_password)
    return render(request, 'generator/password.html', {'password': generated_password})

