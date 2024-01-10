"""
    Module name :- views
    Method(s) :- homepage(), career_page(), join_us(), stuudent_registration(),
    teacher_registration()
"""

from django.shortcuts import render
from academy.forms import StudentForm, TeacherForm
from academy.models import StudentInfo, TeacherInfo


def homepage(request):
    """
    Returns homepage of the website.
    """
    return render(request, "homepage.html")


def career_page(request):
    """
    Returns career page of the website.
    """
    return render(request, "careerpage.html")


def join_us(request):
    """
    Display why to join us.
    """
    return render(request, "joinus.html")


def curriculum(request):
    """
    Display the curriculum.
    """
    return render(request, "lesson.html")


def student_registration(request):
    """
    Store the student data in student model.
    """
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_info = StudentInfo.objects.create(
                name=student_form.cleaned_data.get("name", ""),
                age=student_form.cleaned_data.get("age", 0),
                email=student_form.cleaned_data.get("email", ""),
                phone_no=student_form.cleaned_data.get("phone_no", ""),
            )
            student_info.save()

    student_form = StudentForm()
    return render(request, "register_student.html", {"form": student_form})


def teacher_registration(request):
    """
    Store the teacher data in teacher model.
    """
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)

        if teacher_form.is_valid():
            teacher_info = TeacherInfo.objects.create(
                name=teacher_form.cleaned_data.get("name", ""),
                age=teacher_form.cleaned_data.get("age", 0),
                email=teacher_form.cleaned_data.get("email", ""),
                phone_no=teacher_form.cleaned_data.get("phone_no", ""),
                experience=teacher_form.cleaned_data.get("experience", 0),
            )
            teacher_info.save()

    teacher_form = TeacherForm()
    return render(request, "register_teacher.html", {"form": teacher_form})
