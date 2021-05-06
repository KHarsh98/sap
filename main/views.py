from django.shortcuts import render
import json
from .models import Employee
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if request.method=="POST":
        try:
            json_data = request.read()
            employee_dict = json.loads(json_data)
            print("JSON data successfully grabbed!")

        except:
            print("JSON data was lost.")

        try:
            Employee.objects.create(name=employee_dict['name'],designation=employee_dict['designation'])
            return render(request, 'main/success.html')

        except:
            print("Something went wrong!")
            return render(request, 'main/failure.html')
        finally:
            print("Test complete.")
        
def index(request):
    return render(request, 'main/index.html')