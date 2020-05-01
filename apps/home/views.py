from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from apps.home.mixins import DashboardLoginRequiredMixin


class index(TemplateView):
    template_name = 'home/index.html'


class DashboardView(DashboardLoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'
