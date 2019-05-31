from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def homepage(request):
    return render(request=request,
                 template_name="main/home.html",
                 context={"projects": Project.objects.all})

                 
def card(request):

    cardid = request.GET.get('id', '')
    return render(request=request,
                 template_name="main/card.html",
                 context={"proj": Project.objects.get(id=cardid)})
