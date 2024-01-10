"""
    Module name :- urls
"""

from django.urls import path
from academy import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("career/", views.career_page, name="career"),
    path("joinus/", views.join_us, name="join_us"),
    path("curriculum/", views.curriculum, name="curriculum"),
    path("student-registration/", views.student_registration, name="student_register"),
    path("teacher-registration/", views.teacher_registration, name="teacher_register"),
]
