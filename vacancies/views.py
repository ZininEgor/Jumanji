from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Specialty, Company, Vacancy


class MainView(ListView):
    template_name = "index.html"
    model = Vacancy


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Specialty.objects.values().annotate(count=Count('vacancies')).order_by('-count')
        context['companies'] = Company.objects.values().annotate(count=Count('companies')).order_by('-count')
        return context


class ListVacancies(ListView):
    model = Vacancy
    context_object_name = 'objects'
    template_name = "vacancies.html"


class VacancyBySpecialization(ListView):
    model = Vacancy
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Vacancy.objects.filter(specialty__code=self.kwargs['title'])
        context['specialties'] = get_object_or_404(Specialty, code=self.kwargs['title'])
        return context


class DetailCompany(ListView):
    model = Company
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Company, id=self.kwargs['id'])
        context['vacancies'] = Vacancy.objects.filter(company=get_object_or_404(Company, id=self.kwargs['id']))
        return context


class DetailVacancies(DetailView):
    model = Vacancy
    context_object_name = 'object'
    template_name = "vacancy.html"

    def get_object(self, **kwargs):
        return get_object_or_404(Vacancy, id=self.kwargs['id'])
