from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cc = models.IntegerField(unique=True)  # Cédula de ciudadanía, asegurando que sea única
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de registro automática
    direccion = models.CharField(max_length=100)  # Dirección, ajustada a un tamaño razonable
    telefono = models.CharField(max_length=15)  # Teléfono, usando CharField para permitir diferentes formatos
    grado = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username




class Student(models.Model):
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('N', 'No aplica'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    no_documento = models.CharField(max_length=20)
    grado = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=255)
    padre_familia = models.CharField(max_length=100)
    numero_padre = models.CharField(max_length=15)

    def __str__(self):
       return f"{self.nombre} {self.apellido}"



class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    espanol = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    matematicas = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ingles = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    religion = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sociales = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    etica = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    edu_fisica = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"{self.id} {self.student}"




class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Tardanza', 'Tardanza')])