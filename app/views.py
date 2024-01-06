from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length

def topics (request):
    TO=Topics.objects.all()
    TO=Topics.objects.all().order_by('topic_name')
    TO=Topics.objects.all().order_by('-topic_name')
    TO=Topics.objects.all().order_by(Length('topic_name'))
    TO=Topics.objects.all().order_by(Length('topic_name').desc())
    TO=Topics.objects.all()

    d={'topics' : TO}
    return render(request,'topics.html',d)

def webpage (request):
    WO=Webpage.objects.all()
    WO=Webpage.objects.all().order_by('name')
    WO=Webpage.objects.all()

    d={'webpage' : WO}
    return render (request,'webpage.html',d)

def accessrecord (request):
    AO=Accessrecord.objects.all()
    AO=Accessrecord.objects.all().order_by('author')
    AO=Accessrecord.objects.all().order_by('-author')
    AO=Accessrecord.objects.all().order_by(Length('author'))
    AO=Accessrecord.objects.all().order_by(Length('author').desc())

    d={'accessrecord' : AO}
    return render (request,'accessrecord.html',d)

def insert_topic(request):
    too=input('Enter a Topic : ')
    top=Topics.objects.get_or_create(topic_name=too)[0]
    top.save()

    to=Topics.objects.all()
    d={'topics': to}
    return render(request,'topics.html',d)

def insert_webpage(request):
    wo=input('Enter a Topic : ')
    wn=input('Enter a Name : ')
    wu=input('Enter a URL : ')
    we=input('Enter a Email : ')

    wooo=Topics.objects.get(topic_name=wo)
    woo=Webpage.objects.get_or_create(topic_name=wooo,name=wn,url=wu,email=we)[0]
    woo.save()

    wp=Topics.objects.all()
    d={'webpage':wp}
    return render (request,'webpage.html',d)
