
from django.shortcuts import render
from.models import about,test,Team,testmonial
def home(request):
    aboutdata=about.objects.all()
    testdata=test.objects.all()
    Teamdata=Team.objects.all()
    testmonialdata=testmonial.objects.all()

    context={
        'about':aboutdata,
        'test':testdata,
        'Team':Teamdata,
        'testmonial':testmonialdata,
    }

    return render(request,"home.html",context)
