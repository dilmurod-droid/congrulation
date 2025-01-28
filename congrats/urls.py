from django.urls import path
from . import views
from .views import view_teacher

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher-view',view_teacher,name="view_teacher")
]