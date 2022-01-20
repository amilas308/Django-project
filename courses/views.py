from django.shortcuts import render

# Create your views here.

def our_courses(request):
    return render(request, 'courses.html')
    
    
def cs_courses(request):
    return render(request, 'cs-courses.html')
    
def it_courses(request):
    return render(request, 'it-courses.html')