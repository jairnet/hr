from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.home.mixins import DashboardLoginRequiredMixin
from apps.users.models import Candidate
from apps.users.forms import CandidateForm
from django.views.generic.edit import FormView


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
                return redirect('dashboard')
            else:
                return render(request, 'users/login.html', {'error':'Usuario o Password incorrecto!'})    
            # elif user and instance.
        return render(request, 'users/login.html', {'error':'El usuario {} no existe!'.format(email)})
    return render(request, 'users/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')


def candidateCreateView(request):
    if request.method == 'POST':
        identification = request.POST['identification']
        print('identification>>', identification)
    return render(request, 'users/login.html')


class CandidateListView(DashboardLoginRequiredMixin, ListView):
    model = Candidate
    template_name = 'users/candidate_list.html'

    def get_queryset(self):
        user = self.request.user.id
        query = Candidate.objects.filter(property_of = user)
        return query   
