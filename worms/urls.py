# worms/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from worms.views import MeasurementListAPI, MeasurementListHTML, measurement_csv_view

urlpatterns = [
    path("api/", MeasurementListAPI.as_view()),
    path("csv/", measurement_csv_view, name="download_csv"),
    path("", MeasurementListHTML.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
