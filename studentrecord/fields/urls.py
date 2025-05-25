from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    student_list_view,
    student_name_view,
    student_age_view,
    student_class_view,
    student_marks_view,
    student_roll_view,
    student_update,
    home,
)

app_name = 'students'  # Namespace for app

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('', home, name='home'),  # Set home as root view
    path('list/', student_list_view, name='student_list'),
    path('name/<int:student_id>/', student_name_view, name='student_name'),
    path('age/<int:student_id>/', student_age_view, name='student_age'),
    path('class/<int:student_id>/', student_class_view, name='student_class'),
    path('marks/<int:student_id>/', student_marks_view, name='student_marks'),
    path('rollnumber/<int:student_id>/', student_roll_view, name='student_roll'),
    # URL pattern expects 'id'
   path('update/<int:student_id>/', student_update, name='student_update'),


    # Use direct import here

    path('api/', include(router.urls)),
]
