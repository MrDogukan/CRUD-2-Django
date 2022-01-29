from unicodedata import name
from django.urls import include, path
from .views import home_page, student_delete, student_list, student_add, student_detail, student_update

urlpatterns = [
    path('', home_page, name="home"),
    path('student_list/',student_list, name="list"),
    path('student_add/',student_add, name="add"),
    path('student_detail/<int:id>',student_detail, name="detail"),
    path('student_update/<int:id>', student_update , name="update"),
    path('student_delete/<int:id>', student_delete , name="delete")
]
