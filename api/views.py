from rest_framework import generics,permissions
from .models import Course,Student,Teacher,Grade 
from .serializers import CourseSerializer,StudentSerializer,TeacherSerializer, GradeSerializer, CourseListSerializer, GradeListSerializer
 

class CourseApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = (permissions.AllowAny,)


class CourseCreateApiView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)


class CourseUpdateApiView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)


class CourseDeleteApiView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)



class StudentApiView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

class StudentCreateApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)

class StudentDetailApiView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

class StudentUpdateApiView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)

class StudentDeleteApiView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)



class TeacherApiView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.AllowAny,)

class TeacherCreateApiView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class =TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)

class TeacherDetailApiView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.AllowAny,)

class TeacherUpdateApiView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)

class TeacherDeleteApiView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)


class GradeApiView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer
    permission_classes = (permissions.AllowAny,)

class GradeCreateApiView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)

class GradeDetailApiView(generics.RetrieveAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.AllowAny,)

class GradeUpdateApiView(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)

class GradeDeleteApiView(generics.DestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)