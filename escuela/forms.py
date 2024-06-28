from django import forms
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .models import Teacher, Student, Grade,  Attendance

class TeacherRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ['cc', 'direccion', 'telefono', 'grado']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        teacher = super().save(commit=False)
        teacher.user = user
        if commit:
            teacher.save()
        return teacher


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'nombre', 'apellido', 'edad', 'no_documento', 'grado', 
            'genero', 'direccion', 'padre_familia', 'numero_padre'
        ]



class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['espanol', 'matematicas', 'ingles', 'religion', 'sociales', 'etica', 'edu_fisica']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
AttendanceFormSet = modelformset_factory(Attendance, form=AttendanceForm, extra=0)