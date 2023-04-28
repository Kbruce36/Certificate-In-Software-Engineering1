from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

    
def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            zip_code = form.cleaned_data.get('zip_code')
            if not zip_code.isnumeric() or len(zip_code) != 5:
                messages.error(request, "Invalid zip code. Please enter a valid 5-digit zip code.")
                return render(request, 'index.html', {'form': form})
            form.save()
            messages.success(request, "Your form has been submitted successfully.")
            return redirect('success')
        else:
            messages.error(request, "There was an error in your submission.")
    return render(request, 'index.html', {'form': form})
    

def home(request):
    return render(request, 'home.html')