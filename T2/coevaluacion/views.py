from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, 'landing-page.html')


def profile(request):
    return render(request, 'profile.html')


def profile_student(request):
    return render(request, 'profile-student.html')

def ficha_coev(request):
    return render(request, 'ficha-coev.html')

def ficha_coev_eq_doc(request):
    return render(request, 'ficha-coev-eq-doc.html')


def course_teacher_view(request):
    return render(request, 'course-teacher-view.html')


def course_student_view(request):
    return render(request, 'course-student-view.html')


def login(request):
    return render(request, 'login.html')