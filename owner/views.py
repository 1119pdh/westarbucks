import json
from django.db.models.fields import EmailField

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from owner.models import Owner, Dog

# Create your views here.

class OwnerListView(View):

    def post(self, request):
        input_data = json.loads(request.body)

        Owner.objects.create(
            name = input_data["name"],
            email = input_data["email"],
            age = input_data["age"]

        )
    
        return JsonResponse({"message":"SUCCESS"}, status= 201)

    def get(self, request):
        results = [] 

        owners = Owner.objects.all()
        for owner in owners:
            dogs = owner.dog_set.all()
            dogs_list = []
            for dog in dogs:
                dogs_list.append(
                    {
                        "name" : dog.name,
                        "age" : dog.age
                    }
                )
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age,
                    "dog" : dogs_list
                }
            )
        
        return JsonResponse({"owners" : results}, status= 200)
        


class DogListView(View):
    def post(self, request):
        input_data = json.loads(request.body)
        
        Dog.objects.create(
           name = input_data["name"],
           age = input_data["age"],
           Owner = Owner.objects.get(name = input_data["owner_id"])
        )

        return JsonResponse({"message":"SUCCESS"}, status= 201)

    def get(self, request):
        results = [] 

        dogs = Dog.objects.all()
        for dog in dogs:
            results.append(
                {
                    "Owner" : {
                        "id" : dog.owner.id,
                        "name" : dog.owner.name,
                        "email" : dog.owner.email,
                        "age" : dog.owner.age
                    },
                    "name" : dog.name,
                    "age" : dog.age
                }
            )


        return JsonResponse({"dogs" : results}, status= 200)

    