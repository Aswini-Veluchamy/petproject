from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        policy = request.POST['policy']
        species = request.POST['species']
        age = request.POST['age']
        amount = request.POST['amount']
        variety = request.POST['variety']
        print("working")
        print(policy, species, age, amount, variety)
    else:
        return render(request, "petapp/home.html")