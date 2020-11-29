from django.db import models


class CompanyModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class SpecialtyModel(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.URLField(default='https://place-hold.it/100x60')


class VacancyModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(SpecialtyModel, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
