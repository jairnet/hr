from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('dashboard', views.DashboardAdminView.as_view(), name="dashboard_admin"),
    path('create-candicate', views.CandidateCreateView.as_view(), name="create_candidate"),
    path('list-candidates',views.CandidateListView.as_view(), name="list_candidates"),
    path('detail-candidates/<int:pk>',views.CandidateDetailView.as_view(), name="detail_candidates"),
    

    # path('signup', views.signupView, name="signup"),
]
