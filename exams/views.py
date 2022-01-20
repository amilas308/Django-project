from django.shortcuts import render

# Exams page
# CS Exams page
# IT exams
# SWE exams
# CBS exams
# MIT exams
# PGDCS exams

def allExams(request):
    return render(request, 'allexams.html')

def cs_exams(request):
    return render(request, 'cs-exams.html')

def it_exams(request):
    return render(request, 'it-exams.html')





