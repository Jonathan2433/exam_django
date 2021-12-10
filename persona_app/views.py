from django.shortcuts import render

from django.http import HttpResponse

from .models import Persona

# views to create a new persona
def task_create(request):
    return HttpResponse('Creation d\'un persona')

# views to saw detail of a new persona
<<<<<<< HEAD
def task_details(request, id):
    return HttpResponse(f'Détails d\'un persona id : {id}')
=======
def persona_details(request, id):
    person = Persona.objects.get(id=id)
    context = {
        'person_details': person
    }
    return render(request, 'persona_app/persona_details', context)
>>>>>>> template_details

# views to saw LIST of personas
def task_list(request):
    return HttpResponse('Liste des personas') 