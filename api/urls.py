from django.urls import path
from .views import *


urlpatterns = [

    path('course-list/',CourseApiView.as_view()),
    path('create-course/',CourseCreateApiView.as_view()),
    path('course-detail/<int:pk>/',CourseDetailApiView.as_view()),
    path('update-course/<int:pk>/',CourseUpdateApiView.as_view()),
    path('delete-course/<int:pk>/',CourseDeleteApiView.as_view()),
    
    path('student-list/',StudentApiView.as_view()),
    path('create-student/',StudentCreateApiView.as_view()),
    path('student-detail/<int:pk>/',StudentDetailApiView.as_view()),
    path('update-student/<int:pk>/',StudentUpdateApiView.as_view()),
    path('delete-student/<int:pk>/',StudentDeleteApiView.as_view()),

    
    path('teacher-list/',TeacherApiView.as_view()),
    path('create-teacher/',TeacherCreateApiView.as_view()),
    path('teacher-detail/<int:pk>/',TeacherDetailApiView.as_view()),
    path('update-teacher/<int:pk>/',TeacherUpdateApiView.as_view()),
    path('delete-teacher/<int:pk>/',TeacherDeleteApiView.as_view()),
    
    
    path('grade-list/',GradeApiView.as_view()),
    path('create-grade/',GradeCreateApiView.as_view()),
    path('grade-detail/<int:pk>/',GradeDetailApiView.as_view()),
    path('update-grade/<int:pk>/',GradeUpdateApiView.as_view()),
    path('delete-grade/<int:pk>/',GradeDeleteApiView.as_view()),
]