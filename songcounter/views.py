from django.shortcuts import render
from .models import Songs,Radio,RadioCount

# Create your views here.
def songs(request):
    data = Songs.objects.all()
    # radio = Radio.objects.all()
    radio_count = RadioCount.objects.all()
    context = {
        'songs':data,
        'radio_count':radio_count
    }
    return render(request,'displaysongs.html',context=context)