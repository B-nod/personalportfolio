from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
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

def contact_form(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request)
            return redirect('/')
        else:
            return render(request, 'folio/index.html', {"form":form})
    
    context = {
        "form":ContactForm
    }
    return render(request, 'folio/index.html', context)






