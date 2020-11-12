from django.http import HttpResponse
from django.template import loader
from .models import Persona


def index(request):
    latest_persona_list = Persona.objects.order_by('nombre')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_persona_list': latest_persona_list,
    }
    return HttpResponse(template.render(context, request))