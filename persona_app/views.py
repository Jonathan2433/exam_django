from django.shortcuts import render

from django.http import HttpResponse

from .models import Persona

# views to saw LIST of personas
def persona_list(request):
    personas = Persona.objects.all().order_by('-id')
    context = {
        'personas':personas
    }
    return render(request, 'persona_app/persona_list.html', context)

# views to create a new persona
def persona_create(request):
    return HttpResponse('Creation d\'un persona')

# views to saw detail of a new persona
def persona_details(request, id):
    person = Persona.objects.get(id=id)
    context = {
        'person_details': person
    }
    print(context)
    return render(request, 'persona_app/persona_details.html', context)
