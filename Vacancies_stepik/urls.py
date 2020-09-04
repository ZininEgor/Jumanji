"""Vacancies_stepik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Vacancies_stepik.settings import MEDIA_URL, MEDIA_ROOT
from vacancies.views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('about/', About.as_view()),
    path('admin/', admin.site.urls),
    path('vacancies/', ListVacancies.as_view()),
    path('vacancies/<int:id>/', detail_vacancies),
    path('vacancies/cat/<title>/', VacancyBySpecialization.as_view()),
    path('companies/<int:id>/', DetailCompany.as_view()),
    path('mycompany/vacancies', MyCompanyVacancyView),
    path('mycompany/vacancies/create', create_my_vacancy),
    path('mycompany/vacancies/<str:vacancy_id>', update_my_vacancy),
]

urlpatterns += [
    path('mycompany/', MyCompany, name='MyCompany'),
    path('profile', AccountSettings, name='profile'),
    path('logout', LogoutPage, name='logout'),
    path('login', LoginPage, name='login'),
    path('register/', RegisterPage, name='register'),
    path('myresume/', ResumeEdit, name='myresume')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
