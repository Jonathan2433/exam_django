from django.shortcuts import render

from django.http import HttpResponse

# views to create a new persona
def persona_create(request):
    return HttpResponse('Creation d\'un persona')

# views to saw detail of a new persona
def persona_details(request, id):
    return HttpResponse(f'Détails d\'un persona id : {id}')

# views to saw LIST of personas
def persona_list(request):
    return HttpResponse('Liste des personas') 