from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        models = Course.objects.all()
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        models = Teacher.objects.all()
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Student.objects.all()
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Grade.objects.all()
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    teachers = serializers.StringRelatedField(many=True)
    class Meta:
        models = Course.objects.all()
        fields = ['id', 'title', 'start_at', 'cost', 'students', 'teachers']


class GradeListSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=False)
    course = serializers.StringRelatedField(many=False)
    class Meta:
        model = Grade.objects.all()
        fields = ['grade_value','date','student','course']