from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from vacancies_app.models import SpecialtyModel, VacancyModel, CompanyModel


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... 404!')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... 500!')


class MainView(View):
    def get(self, request):
        specialties = SpecialtyModel.objects.all()

        vacancies = VacancyModel.objects.all()
        companies = CompanyModel.objects.all()
        vacancy_cnt = {}
        company_cnt = {}
        for specialty in specialties:
            vacancy_cnt[specialty] = vacancies.filter(specialty_id=specialty.id).count()
        for company in companies:
            company_cnt[company] = vacancies.filter(company_id=company.id).count()
        context = {'vacancy_cnt': vacancy_cnt, 'company_cnt': company_cnt}
        return render(request, 'index.html', context=context)


class VacanciesList(View):
    def get(self, request):
        vacancies = VacancyModel.objects.all()
        for vacancy in vacancies:
            lst = vacancy.skills.split(',')
            vacancy.skills = ' •'.join(lst)
        return render(request, 'vacancies.html', {'vacancies': vacancies})


class SpecialtyVacancy(View):
    def get(self, request, code):
        vacancies = VacancyModel.objects.filter(specialty__code=code)
        context = {'speciality': SpecialtyModel.objects.all().get(code__exact=code),
                   'vacancies': vacancies}
        return render(request, 'vacancies_specialization.html', context=context)


class Company(View):
    def get(self, request, company_id):
        vacancies = VacancyModel.objects.filter(company__id=company_id)
        context = {'company': CompanyModel.objects.all().get(id__exact=company_id),
                   'vacancies': vacancies}
        return render(request, 'company.html', context=context)


class Vacancy(View):
    def get(self, request, vacancy):
        vacancy = VacancyModel.objects.get(id__exact=vacancy)
        return render(request, 'vacancy.html', {'vacancy': vacancy})
