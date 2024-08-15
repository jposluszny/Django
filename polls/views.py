from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from . models import Question
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class QuestionListView(ListView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    fields = '__all__'

