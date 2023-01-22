from django.shortcuts import render
from .models import Place,Person
from django.http import HttpResponse

def demo(request):
    obj=Place.objects.all()
    pe=Person.objects.all()

    return render(request,'index.html',{'result':obj,'person':pe})