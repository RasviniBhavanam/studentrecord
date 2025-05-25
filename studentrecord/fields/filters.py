import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    min_marks = django_filters.NumberFilter(field_name="marks", lookup_expr='gte', label="Minimum Marks")
    max_marks = django_filters.NumberFilter(field_name="marks", lookup_expr='lte', label="Maximum Marks")
    student_class = django_filters.CharFilter(field_name="student_class", lookup_expr='icontains', label="Class")

    class Meta:
        model = Student
        fields = ['student_class', 'min_marks', 'max_marks']

