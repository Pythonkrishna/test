from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q
# Create your views here.
def student_list(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,"display.html",{"posts":posts})

def student_list(request):
    posts = Student.objects.filter(Q(surname__istartswith='a')| Q(surname__istartswith='k'))
    print(posts)
    print(connection.queries)
    return render(request,"display.html",{"posts":posts})

def student_list(request):
    posts = Student.objects.filter(classroom=4) &Student.objects.\
        filter(firstname__istartswith='v')
    #posts = Student.objects.exclude(classroom=4) & Student.objects. \
        #filter(firstname__istartswith='v')
    print(posts)
    print(connection.queries)

    return render(request,"display.html",{'posts':posts})



def student_list(request):
    posts = Student.objects.all().values_list("firstname").union\
        (Teacher.objects.all().values_list("firstname"))

    print(posts)
    print(posts.query)
    return render(request,"display.html",{"posts":posts})