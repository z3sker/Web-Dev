from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view()),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view()),
    path('companies/<int:id>/vacancies/', views.CompanyVacanciesView.as_view()),

    path('vacancies/', views.VacancyListView.as_view()),
    path('vacancies/<int:pk>/', views.VacancyDetailView.as_view()),
    path('vacancies/top_ten/', views.TopTenVacanciesView.as_view()),
]