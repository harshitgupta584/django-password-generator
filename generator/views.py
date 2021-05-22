from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html")

def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    your_password = ''
    length = int(request.GET.get('length',12)) # 12 is default length
    
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()_+=_[]{}|\?/><.,'))
    
    if request.GET.get('numbers'):
        char.extend(list('1234567890'))    


    for i in range(length):
        your_password += random.choice(char)
    return render(request,"generator/password.html",{'password':your_password})


def about(request):
    return render(request,"generator/about.html")
