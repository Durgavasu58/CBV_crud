from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.generic.edit import FormView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


class HomePage(TemplateView):
	template_name='home.html'


class StudentFormView(FormView):
	form_class = StudentForm
	template_name = 'studentform.html'
	success_url = reverse_lazy('cbvapp:retrivedata')
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class StudentListView(ListView):
	model = Student
	template_name='detail.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name='update.html'
    success_url = reverse_lazy('cbvapp:retrivedata')
class StudentDeleteView(DeleteView):
	model = Student
	template_name='delete.html'
	success_url = reverse_lazy('cbvapp:retrivedata')



