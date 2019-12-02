from django.shortcuts import render
from .models import Songs

# Create your views here.
def songs(request):
    data = Songs.objects.all()
    context = {
        'songs':data
    }
    return render(request,'displaysongs.html',context=context)