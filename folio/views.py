from django.shortcuts import render, redirect
from . models import *
# Create your views here.

def homepage(request):
    prot = Prot.objects.all()
    skill = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    client = Client.objects.all()
    project = Project.objects.all()

    context = {
        'prot': prot,
        'skill':skill,
        'education':education,
        'experience': experience,
        'client':client,
        'project':project
    }
    return render(request, 'folio/index.html', context)