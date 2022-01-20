from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty

def index(request):
    
    facs = Faculty.objects.all()
    
    context = {
        'facs':facs
    }
    return render(request, 'index.html', context)
    

def create_faculty(request):
    
    form = FacultyForm()
    if request.method=="POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create/faculty/')
    
    context = {
        'form': form
    }    
    return render(request, 'create-faculty.html', context)
 


def all_faculties(request):
    facs = Faculty.objects.all()
    context = {
        'facs': facs
    }    
    return render(request, 'all_faculties.html', context)


def faculty_details(request, id):
    faculty = Faculty.objects.get(id = id)
    context = {
        'faculty': faculty
    }    
    return render(request, 'faculty-details.html', context)



def update_faculty(request, id):
    
    faculty = Faculty.objects.get(id=id)
    form = FacultyForm(instance=faculty)
    if request.method=="POST":
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            
            return redirect('/create/faculty/')
    
    context = {
        'form': form,
        'faculty': faculty
    }    
    return render(request, 'update-faculty.html', context)
    
    
def faculty_delete(request, id):
    faculty = Faculty.objects.get(id = id)
    faculty.delete()
    
    
def events(request):
    
    facs = Faculty.objects.all()