from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from rest_framework import viewsets, filters
from .filters import StudentFilter
from .serializers import StudentSerializer


def home(request):
    return render(request, 'fields/home.html')  # Make sure this template exists


# DRF ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_class = StudentFilter
    search_fields = ['name', 'student_class']
    ordering_fields = ['marks', 'name']


# HTML views
def student_list_view(request):
    students = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=students)
    return render(request, 'fields/list.html', {'filter': student_filter, 'students': student_filter.qs})

def student_list(request):
    student_class = request.GET.get('student_class', '')
    min_marks = request.GET.get('min_marks')
    max_marks = request.GET.get('max_marks')

    students = Student.objects.all()

    if student_class:
        students = students.filter(student_class__icontains=student_class)
    if min_marks:
        students = students.filter(marks__gte=min_marks)
    if max_marks:
        students = students.filter(marks__lte=max_marks)

    return render(request, 'fields/list.html', {'students': students})



def student_age_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'fields/age.html', {'student': student})


def student_name_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'fields/name.html', {'student': student})


def student_class_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'fields/class.html', {'student': student})


def student_marks_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'fields/marks.html', {'student': student})


def student_roll_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'fields/rollnumber.html', {'student': student})


def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.student_class = request.POST['student_class']
        student.age = request.POST['age']
        student.marks = request.POST['marks']
        student.roll_number = request.POST['roll_number']
        student.save()
        return redirect('students:home')  # Adjust as needed

    return render(request, 'fields/update.html', {'student': student})
