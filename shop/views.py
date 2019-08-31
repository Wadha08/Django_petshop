from django.shortcuts import render,redirect
from .models import Pet
from .forms import PetForm

def pet_list(request):
	pets = Pet.objects.all()
	context = {
		"pets": pets,
	}
	return render(request, 'list.html', context)


def pet_detail(request, pet_id):
	pet = Pet.objects.get(id=pet_id)
	context = {
		"pet": pet,
	}
	return render(request, 'detail.html', context)


def pet_create(request):
	form = PetForm()
	if request.method == "POST":
		form = PetForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			return redirect('pet-list')
	context = {
		"form": form,
	}
	return render(request, 'create.html' , context)


def pet_update(request, pet_id):
	Pet_obj = Pet.objects.get(id=pet_id)
	form = PetForm(instance = Pet_obj)
	if request.method == "POST":
		form = PetForm(request.POST , instance=Pet_obj)
		if form.is_valid():
			form.save()
			return redirect('pet-list')
	context = {
        "Pet_obj": Pet_obj,
        "form": form,
    }
	return render(request, 'update.html', context)



def pet_delete(request, pet_id):
	Pet_obj = Pet.objects.get(id=pet_id)
	Pet_obj.delete()
	return redirect('pet-list')

