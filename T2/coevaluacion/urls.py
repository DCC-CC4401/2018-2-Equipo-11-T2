from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('landing-page/', views.landing_page, name='landing_page'),
    path('landing-page-teacher/', views.landing_page_teacher, name='landing_page_teacher'),
    path('profile/', views.profile, name='profile'),
    path('profile-student/', views.profile_student, name='profile_student'),
    path('ficha-coev/', views.ficha_coev, name='ficha_coev'),
    path('ficha-coev-eq-doc/', views.ficha_coev_eq_doc, name='ficha_coev_eq_doc'),
    path('course-teacher/', views.course_teacher_view, name='teacher_course'),
    path('course-student/', views.course_student_view, name="student_course"),
]
