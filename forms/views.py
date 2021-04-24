from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    if request.method == "POST":
        usn = request.POST.get('usn', '')
        name = request.POST.get('name', '')
        semester = request.POST.get('semester', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        if usn and name and semester and mobile and email:
            contact = Contact(usn=usn,name=name,semester=semester,mobile=mobile,email=email)
            contact.save()
        else:
            return HttpResponse("Please enter all the details")

    return render(request,'index.html')
