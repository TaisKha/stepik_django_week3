from django.db import models


class Company(models.Model):

    def __str__(self):
        return f'{self.name}'

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    def __str__(self):
        return f'{self.code} {self.title}'

    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    def __str__(self):
        return f'{self.title}'

    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
