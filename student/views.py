from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from django.urls import reverse_lazy


class Home_Page(ListView):
    model = Student
    template_name = "home.html"
    context_object_name = "HomePage"


class StudentCreate(CreateView):
    model = Student
    fields = ('First_Name', 'Middle_Name', 'Last_Name', 'Age', 'Gender', 'Address', 'Email', 'Mobile',
              'Alternate_Email', 'Alternate_Mobile', 'Father_Name', 'Mother_Name', 'Institute_Name', 'Branch_Name')
    template_name = 'student/create_form.html'
    context_object_name = "CreateForm"
    success_url = reverse_lazy("home_page")


class StudentUpdate(UpdateView):
    model = Student
    fields = ('First_Name', 'Middle_Name', 'Last_Name', 'Age', 'Gender', 'Address', 'Email', 'Mobile',
              'Alternate_Email', 'Alternate_Mobile', 'Father_Name', 'Mother_Name', 'Institute_Name', 'Branch_Name')
    template_name = 'student/update_form.html'
    context_object_name = "UpdateForm"
    success_url = reverse_lazy("home_page")


class StudentDetails(DetailView):
    model = Student
    fields = ('First_Name', 'Middle_Name', 'Last_Name', 'Age', 'Gender', 'Address', 'Email', 'Mobile',
              'Alternate_Email', 'Alternate_Mobile', 'Father_Name', 'Mother_Name', 'Institute_Name', 'Branch_Name')
    template_name = 'student/details_form.html'
    context_object_name = "DetailForm"


class StudentDelete(DeleteView):
    model = Student
    template_name = 'student/delete_form.html'
    context_object_name = "DeleteForm"
    success_url = reverse_lazy("home_page")
