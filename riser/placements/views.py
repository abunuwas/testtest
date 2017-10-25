from django.http import HttpResponse, JsonResponse

from . import models


def index(request):
    #placement = models.Placement.objects.all()[0]
    return JsonResponse({
        'status': 'hired',
        'Reference': '1234',
        'Company':  'Fake',
        'Candidate': 'Dick',
        'Start': 'Tomorrow',
        'End': 'After tomorrow'
    })
