from django.shortcuts import render
from forms import StudentForm, TeacherForm
from models import StudentInfo, TeacherInfo

def homepage(request):
    return render(request, 'homepage.html')

def career_page(request):
    return render(request, 'careerpage.html')

def join_us(request):
    return render(request, 'joinus.html')

def student_registration(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        
        student_info = StudentInfo.objects.create(
            name = student_form.get('name', ''),
            age = student_form.get('age', 0),
            email = student_form.get('email', ''),
            phone_no = student_form.get('phone_no', '')
        )
        student_info.save()

        return request(request, 'register_student.html', {'form': student_form})

    student_form = StudentForm()
    return render(request, 'register_student.html', {'form': student_form})

def teacher_registration(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        
        teacher_info = TeacherInfo.objects.create(
            name = teacher_form.get('name', ''),
            age = teacher_form.get('age', 0),
            email = teacher_form.get('email', ''),
            phone_no = teacher_form.get('phone_no', ''),
            experience = teacher_form.get('experience', 0)
        )
        teacher_info.save()

        return request(request, 'register_teacher.html', {'form': teacher_form})

    teacher_form = TeacherForm()
    return render(request, 'register_teacher.html', {'form': teacher_form})