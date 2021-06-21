import json
from django.views import View
from django.http import JsonResponse
from .models import Owner, Dog

class OwnerView(View):
	def get(self, request):
		owners = Owner.objects.all()
		
		result = []
		for owner in owners:
			dogs = owner.dog_set.all() #모델클래스dog을 소문자로 해서 _set 역참조
			dogs_list = []
			for dog in dogs:
				dog_info = {
					'name' : dog.name,
					'age'  : dog.age
				}
				dogs_list.append(dog_info)

			owner_info = {
				'email' : owner.email,
				'name'  : owner.name,
				'age'   : owner.age,
				'dogs'  : dogs_list
			}

			result.append(owner_info)
				
		return JsonResponse({'result': result}, status=200)



	def post(self, request):
		data = json.loads(request.body)

		Owner.objects.create(
			name  = data['name'],
			email = data['email'],
			age   = data['age']
		)

		return JsonResponse({'message':'SUCCESS'}, status=201)
	

class DogView(View):
	def post(self, request):
		data  = json.loads(request.body)
			
		owner = Owner.objects.get(email=data['owner'])
		Dog.objects.create(
			name  = data['name'],
			age   = data['age'],
			owner = owner
		)
		return JsonResponse({'message':'SUCCESS'}, status=201)



	def get(self, request):
		dogs = Dog.objects.all()
		
		result = []
		for dog in dogs:
			dog_info = {
				'owner' : dog.owner.name,
				'name'  : dog.name,
				'age'   : dog.age,
			}

			result.append(dog_info)
		return JsonResponse({'result': result}, status=200)
