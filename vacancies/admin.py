from django.contrib import admin
from .models import Vacancy, Company, Specialty, Application, Resume, StatusModel, GradeModel

class VacancyAdmin(admin.ModelAdmin):
    pass




class CompanyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass



admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume)
admin.site.register(GradeModel)
admin.site.register(StatusModel)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Application, ApplicationAdmin)
