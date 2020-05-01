from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('create-candicate', views.candidateCreateView, name="create_candidate"),
    path('lista',views.CandidateListView.as_view(), name="lista"),
    # path('signup', views.signupView, name="signup"),
]
