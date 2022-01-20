from django.shortcuts import render


def buk_students(request):
    return render(request, 'buk_students.html')
    
   
def about_us(request):
    return render(request, 'about.html')
    
