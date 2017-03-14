import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import Developer
import datetime
from datetime import timedelta


# Create your views here.

def index(request):
    developers = Developer.objects.all().order_by('date')
    for dev in developers:
        if dev.date == datetime.datetime.today().date():
            dev.isNobetci=True
    return render(request, 'welcome/index.html', {
        'developers': developers
    })

class DevDate(object):
    developer = Developer()
    date = datetime.date

    # The class "constructor" - It's actually an initializer
    def __init__(self, developer, date):
        self.developer = developer
        self.date = date

def make_student(name, age, major):
    student = Student(name, age, major)
    return student


def addDeveloper(request):
    mDate = datetime.datetime.strptime(request.GET["date"], '%d%m%y').date()
    d = Developer(name=request.GET["name"], date=mDate)
    d.save()
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })

def deleteDeveloper(request):
    mDate = datetime.datetime.strptime(request.GET["date"], '%d%m%y').date()
    d = Developer.objects.filter(name__exact=request.GET["name"]).filter(date__exact=mDate)
    d.delete()
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })


def nobetcify(request):
    Developer.objects.all().update(isNobetci=False)
    Developer.objects.filter(name__exact=request.GET["name"]).update(isNobetci=True)
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })


def health(request):
    return HttpResponse(PageView.objects.count())
