from django.shortcuts import render

from django.http import HttpResponse

from .models import Persona
import requests
import json



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

# generae by randomuser a new persona
def generate_persona(request):
    # API Call
    res = requests.get('https://randomuser.me/api?nat=fr')
    #  transform to json
    jsonRes = res.json()
    # save results in data
    data = jsonRes['results'][0]
    # save all data we need
    gender = data['gender']
    first_name = data['name']['first']
    last_name = data['name']['last']
    address_street = data['location']['street']['name']
    address_number = data['location']['street']['number']
    city = data['location']['city']
    country = data['location']['country']
    postcode = data['location']['postcode']
    email = data['email']
    username = data['login']['username']
    password = data['login']['password']
    age = data['dob']['age']
    picture = data['picture']['thumbnail']

    persona = Persona()
    persona.first_name = first_name
    persona.last_name = last_name
    persona.address_street = address_street
    persona.address_number = address_number
    persona.city = city
    persona.country = country
    persona.postcode = postcode
    persona.email = email
    persona.username = username
    persona.password = password
    persona.age = age
    persona.picture = picture

    persona.save()

    last_persona_id = Persona.objects.latest('id')
    print('===============================================')
    print(last_persona_id)
    print('===============================================')

    context = {
    'person_details': last_persona_id
    }
    return render(request, 'persona_app/persona_details.html', context)
     
    # if res:
    #     print('ok mon pote')
    # else:
    #     print('pas bon poto')
    








    # return HttpResponse(f'Géneration d\'un persona via randomuser')
    
