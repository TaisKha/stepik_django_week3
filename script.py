import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_django_week3.settings'
django.setup()

from vacancies_app.models import CompanyModel, SpecialtyModel, VacancyModel
from data import jobs, companies, specialties

from datetime import datetime

if __name__ == '__main__':
    SpecialtyModel.objects.all().delete()
    CompanyModel.objects.all().delete()
    VacancyModel.objects.all().delete()

    for specialty in specialties:
        specialty_ = SpecialtyModel.objects.create(
            code=specialty['code'],
            title=specialty['title'],

        )
    for company in companies:
        company_ = CompanyModel.objects.create(
            id=int(company['id']),
            name=company['title'],
            location=company['location'],
            logo=company['logo'],
            description=company['description'],
            employee_count=int(company['employee_count']),
        )
    for job in jobs:
        specialty_ = SpecialtyModel.objects.get(code=job['specialty'])
        company_ = CompanyModel.objects.get(id=int(job['company']))
        job_ = VacancyModel.objects.create(
            id=int(job['id']),
            title=job['title'],
            specialty=specialty_,
            skills=job['skills'],
            description=job['description'],
            salary_max=int(job['salary_to']),
            salary_min=int(job['salary_from']),
            published_at=datetime.strptime(job['posted'], '%Y-%m-%d').date(),
            company=company_,
        )
