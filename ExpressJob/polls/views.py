from django.http import HttpResponse
from django.template import loader
from .models import Persona


def index(request):
    latest_persona_list = Persona.objects.order_by('nombre')
    output = ', '.join([p.nombre for p in latest_persona_list])
    return HttpResponse(output)
