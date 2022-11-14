"""from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  HttpResponse(template.render())"""
#changing the content to that is below

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader

from .models import students


# Create your views here.
def index(request):
    list = students.objects.all()    
    return render(request,'index.html',{"list": list}) # to call the view we must use URL

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({},request)) 

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  student = students(firstname=x, lastname=y)
  student.save()
  return HttpResponseRedirect(reverse('index')) 

def delete(request, id):
  student = students.objects.get(id=id)
  student.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  student = students.objects.get(id=id)
  template = loader.get_template('update.html')  
  context = {
    'student':student,
  }
  return HttpResponse(template.render(context,request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  student = students.objects.get(id=id)
  student.firstname = first
  student.lastname = last
  student.save() 
  return HttpResponseRedirect(reverse('index')) 