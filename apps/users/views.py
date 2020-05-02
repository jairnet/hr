from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.users.mixins import DashboardLoginRequiredMixin
from apps.users.models import Candidate
from django.views import View
from django.views.generic.edit import FormView
import requests
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from apps.users.models import Candidate


def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        instance = User.objects.filter(email=email)
        if len(instance) == 1:
            username = instance[0].username        
            user = authenticate(request, username=username, password=password)
            if user and instance[0].is_staff:
                login(request, user)
                return redirect('dashboard_admin')
            else:
                return render(request, 'users/login.html', {'error':'Usuario o Password incorrecto!'})
        return render(request, 'users/login.html', {'error':'El usuario {} no existe!'.format(email)})
    return render(request, 'users/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')


class DashboardAdminView(DashboardLoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard_admin.html'


class CandidateListView(DashboardLoginRequiredMixin, ListView):
    model = Candidate
    template_name = 'candidate_list.html'

    def get_queryset(self):
        queryset = Candidate.objects.all()
        return queryset


class CandidateDetailView(DashboardLoginRequiredMixin, DetailView):
    model = Candidate
    template_name = 'candidate_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CandidateDetailView, self).get_context_data(**kwargs)
        return context


class CandidateCreateView(View):
    template_name = 'users/candidate_form.html'

    def post(self, request, *args, **kwargs):
        pass

# def candidateCreateView(request):
#     if request.method == 'POST':
#         type_document = request.POST['type_document']
#         identification = request.POST['identification']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         user_name = first_name[:1] + last_name.split()[0]
#         print('user_name', user_name)
#         # user_object = User(username=username, password=password)
#         # p.save()
#     return render(request, 'users/login.html')
