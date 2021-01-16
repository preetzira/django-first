from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'Apple':'Apple is a good company'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact(fname=fname,lname=lname,city=city,username=username,state=state,zip=zip,date=datetime.today())
        contact.save()
        messages.success(request,'Contact has been saved successfully')
    return render(request, 'contact.html')
