import csv
from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from rest_framework import generics, permissions

from worms.models import Measurement
from worms.serializers import MeasurementSerializer


class MeasurementListAPI(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MeasurementListHTML(ListView):
    model = Measurement


def measurement_csv_view(request: HttpRequest) -> HttpResponse:
    timestamp = datetime.now().strftime(r"%Y%m%d%H%M")
    response = HttpResponse(
        content_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=measurements_{timestamp}.csv"
        },
    )

    objects = Measurement.objects.all()

    writer = csv.writer(response)
    writer.writerow([field.name for field in Measurement._meta.get_fields()])
    writer.writerows(
        [
            [record.insert_timestamp, record.humidity, record.temperature]
            for record in objects
        ]
    )

    return response
