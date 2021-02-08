from django.shortcuts import render
from.models import about
def aboutus(request):
    aboutdata=about.objects.all()
    context={
        'about':aboutdata
    } 
    return render(request,'about.html',context)
