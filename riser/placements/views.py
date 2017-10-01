from django.http import HttpResponse, JsonResponse

from . import models


def index(request):
    placement = models.Placement.objects.all()[0]
    return JsonResponse({
        'status': placement.status,
        'Reference': placement.reference,
        'Company':  placement.company.name,
        'Candidate': placement.candidate.first_name,
        'Start': placement.start_date,
        'End': placement.end_date
    })