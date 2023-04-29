from django.shortcuts import render
from home.models import events

# Create your views here.
def index(request):
     
    
    return render(request,'index.html')

def show(request):
    myevents = events.objects.all()
    context = {'event':myevents}
    return render(request,'show.html',context)

