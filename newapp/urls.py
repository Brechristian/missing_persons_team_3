from django.urls import path
from .views import indexPageView, aboutPageView, searchPageView, missing_personsPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about/', aboutPageView, name='about'),
    path('search/', searchPageView, name='search'),
    path('missingperson/<missing_person_id>/',
         missing_personsPageView, name='missing_person_details'),
]
