from django.db import models
from django.urls import reverse

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_surname = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    student_img = models.ImageField(upload_to='images', default='/media')

    def __str__(self) -> str:
        return self.student_name + " " + self.student_surname
    

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_surname = models.CharField(max_length=50)
    teacher_email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    teacher_img = models.ImageField(upload_to='images', default='/media')

    def __str__(self) -> str:
        return self.teacher_name + " " + self.teacher_surname
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    start_at = models.DateTimeField()
    cost = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name='courses')
    teachers = models.ManyToManyField(Teacher, related_name='courses')
    

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})
    

class Grade(models.Model):

    GRADES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='grades', on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=50, choices=GRADES)

    class Meta:
        verbose_name = ("Grade")
        verbose_name_plural = ("Grades")

    def __str__(self):
        return self.grade_value

    def get_absolute_url(self):
        return reverse("Grade_detail", kwargs={"pk": self.pk})

