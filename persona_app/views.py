from django.shortcuts import render

from django.http import HttpResponse

from .models import Persona

<<<<<<< HEAD
=======
# views to saw LIST of personas
def persona_list(request):
    personas = Persona.objects.all().order_by('-id')
    context = {
        'personas':personas
    }
    return render(request, 'persona_app/persona_list.html', context)

>>>>>>> 75547530856b8cae407d7f896a64c62bb4e00ee7
# views to create a new persona
def persona_create(request):
    return HttpResponse('Creation d\'un persona')

# views to saw detail of a new persona
<<<<<<< HEAD
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
=======
def persona_details(request, id):
    return HttpResponse(f'Détails d\'un persona id : {id}')
>>>>>>> 75547530856b8cae407d7f896a64c62bb4e00ee7
