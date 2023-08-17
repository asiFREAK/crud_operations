from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def main_html(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        obj1 = Student.objects.create(name=name, email=email, phone=phone, password=password, confirm_password=confirm_password)
    
        obj1.save()
        # if password != confirm_password:
        #     # context = {'error': 'Passwords do not match'}
            
        #     return render(request,'registration.html', context)
    return render(request,'registration.html')

def view_html(request):
    items = Student.objects.all()
    return render(request, 'details.html', {'items': items})

