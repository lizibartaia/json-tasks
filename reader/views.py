from django.shortcuts import render
from .models import Reader

# Create your views here.

def enter_personal_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        reader = Reader(name=name, email=email, phone_number=phone_number, address=address)
        reader.save()
        return render(request, 'reader/success.html')
    return render(request, 'reader/form.html')