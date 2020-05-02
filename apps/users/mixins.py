from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
