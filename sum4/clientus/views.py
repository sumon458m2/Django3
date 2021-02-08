from django.shortcuts import render
from.models import client
def clientus(request):
    clientdata=client.objects.all()
    context={
        'client':clientdata
    }
    return render(request,'client.html',context)
