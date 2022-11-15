from django.urls import path
from .views import indexPageView, aboutPageView, missing_personsPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about/', aboutPageView, name='about'),
    path('missingpersons/<missing_persons_id>/',
         missing_personsPageView, name="missing_persons_detailed"),
]
