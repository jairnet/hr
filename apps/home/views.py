from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class index(TemplateView):
    template_name = 'home/index.html'
