from django.shortcuts import render, redirect
from server.models import user_registration
from django.contrib import messages
from datetime import datetime

class functions():
  def calculate_age(date_of_birth):
    today = datetime.today()
    birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
class Data_entry(functions):
 def signup(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = int(request.POST.get('age'))
            date_of_birth = request.POST.get('date_of_birth')
            calculated_age = functions.calculate_age(date_of_birth)
            data = user_registration.objects.filter(Email=email)
            if len(data) != 0:
                messages.success(request, 'Email already present on the Database with below details')
                return render(request, 'Your_details.html', {'users': data}) 
            if age <= 0:
                    messages.success(request, 'Invalid Age')
                    return render(request, 'input.html')   
            if age != calculated_age:  
                messages.success(request, 'Age and Date of Birth are Mismatched')
                return render(request, 'input.html')
            user_data = user_registration(Name=name, Email=email, Age=age, Date_of_Birth=date_of_birth)
            user_data.save()
            return redirect('Your_details') 
    except:
        pass
    return render(request, 'index.html')
 def Your_details(request):
    users = user_registration.objects.all()
    return render(request, 'Your_details.html', {'users': users})
