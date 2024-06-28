from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_teacher_view, name='register'),
    path('teacher/', views.view_teachers, name='teacher'),
    path('home/', views.home_view, name='home'),
    path('teacher/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('register_student/', views.register_student_view, name='register_student'),
    path('student/', views.view_students, name='student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('student/edit/<int:pk>/', views.edit_student_view, name='edit_student'),
    path('escuela/manage-grades/<int:student_id>/', views.manage_grades_view, name='manage_grades'),
    path('take-attendance/', views.take_attendance_view, name='take_attendance'),
    path('list_attendace/', views.view_attendance, name='view_attendance'),
    path('delete-attendance/<int:pk>/', views.delete_attendance_view, name='delete_attendance'),
    path('logout/', views.logout_view, name='logout'),
]
