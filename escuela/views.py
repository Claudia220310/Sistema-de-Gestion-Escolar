from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import TeacherRegistrationForm, StudentRegistrationForm, GradeForm, AttendanceFormSet, AttendanceForm
from .models import Teacher, Student, Grade, Attendance
from decimal import Decimal
from django.http import HttpResponse
from django.utils.timezone import now


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, intenta nuevamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def is_admin(user):
    return user.is_superuser

def logout_view(request):
    logout(request)
    return redirect('login') 



@login_required
def register_teacher_view(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'register.html', {'form': form})





@login_required
def home_view(request):
    if request.user.is_superuser:
        students = Student.objects.all()
        return render(request, 'home.html')
    else:
        students = Student.objects.all()  # Asumiendo que obtienes todos los estudiantes
        return render(request, 'homeTeacher.html', {'students': students})



@login_required
def manage_grades_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    grade, created = Grade.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página de estudiantes registrados
    else:
        form = GradeForm(instance=grade)

    return render(request, 'manage_grades.html', {'form': form, 'student': student})


@login_required
def view_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})

@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.user.delete()
        return redirect('teacher')
    return render(request, 'teacher_delete.html', {'teacher': teacher})



@login_required
def register_student_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

@login_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student')
    return render(request, 'student_delete.html', {'student': student})

@login_required
def edit_student_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentRegistrationForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})




@login_required
def take_attendance_view(request):
    students = Student.objects.all()
    today = now().date()  # Obtener la fecha actual

    if request.method == 'POST':
        for student in students:
            fecha = request.POST.get(f'date_{student.id}')
            asistencia = request.POST.get(f'asistencia_{student.id}')

            # Guardar la asistencia en la base de datos
            Attendance.objects.create(
                student=student,
                date=fecha,
                status=asistencia
            )

        # Redirigir a alguna página de éxito o a la misma página
        return redirect('view_attendance')

    context = {
        'students': students,
        'today': today
    }
    return render(request, 'take_attendance.html', context)


@login_required
def view_attendance(request):
    attendances = Attendance.objects.all().select_related('student')  # Obtener todas las asistencias con la información del estudiante

    context = {
        'attendances': attendances
    }
    return render(request, 'view_attendance.html', context)





@login_required
def delete_attendance_view(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    
    if request.method == 'POST':
        attendance.delete()
        return redirect('view_attendance')  # Redirigir a la vista de historial de asistencia
    
    context = {
        'attendance': attendance,
    }
    return render(request, 'delete_attendance.html', context)