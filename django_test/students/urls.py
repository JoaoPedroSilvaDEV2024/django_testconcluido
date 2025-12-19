from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentWithCoursesListView,
)

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),

    # ===== TAREFA 2 =====
    path('with-courses/', StudentWithCoursesListView.as_view(), name='with-courses'),
]
