from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from vacancies_app.models import Specialty, Vacancy, Company


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... 404!')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... 500!')


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()

        vacancies = Vacancy.objects.all()
        companies = Company.objects.all()
        vacancy_cnt = {}
        company_cnt = {}
        for specialty in specialties:
            vacancy_cnt[specialty] = vacancies.filter(specialty_id=specialty.id).count()
        for company in companies:
            company_cnt[company] = vacancies.filter(company_id=company.id).count()
        context = {'vacancy_cnt': vacancy_cnt, 'company_cnt': company_cnt}
        return render(request, 'index.html', context=context)


class VacanciesListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', {'vacancies': vacancies})


class SpecialtyVacancyView(View):
    def get(self, request, code):
        vacancies = Vacancy.objects.filter(specialty__code=code)
        context = {'speciality': Specialty.objects.all().get(code__exact=code),
                   'vacancies': vacancies}
        return render(request, 'vacancies_specialization.html', context=context)


class CompanyView(View):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company__id=company_id)
        context = {'company': Company.objects.all().get(id__exact=company_id),
                   'vacancies': vacancies}
        return render(request, 'company.html', context=context)


class VacancyView(View):
    def get(self, request, vacancy):
        vacancy = Vacancy.objects.get(id=vacancy)
        return render(request, 'vacancy.html', {'vacancy': vacancy})
