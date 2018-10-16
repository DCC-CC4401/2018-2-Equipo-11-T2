from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('ficha-coev/', views.ficha_coev, name='ficha_coev'),
    path('course/teacher/', views.course_teacher_view, name='teacher_course'),
    path('course/student/', views.course_student_view, name="student_course")
]
