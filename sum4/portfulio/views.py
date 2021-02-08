
from django.shortcuts import render
from.models import portfulio
def portfulios(request):
    portfuliodata=portfulio.objects.all()
    context={
        'portfulio':portfuliodata
    }
    return render(request,'portfulio.html',context)
