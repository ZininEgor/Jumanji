from django.contrib import admin
from .models import Vacancy, Company, Specialty, Application, Resume, StatusModel, GradeModel


admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(GradeModel)
admin.site.register(StatusModel)
admin.site.register(Company)
admin.site.register(Specialty)
admin.site.register(Application)
