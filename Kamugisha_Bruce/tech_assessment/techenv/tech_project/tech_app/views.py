from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("your form has been submitted successfully."))
            return redirect('home')
            
        else:
            messages.success(request, "there was an error in your submission.")
            return render(request,'index.html')
          
        #always remember to redirect to a view that handles the page and not the page
    else:
        return render(request, 'index.html', {'form':form})
    

def home(request):
    return render(request, 'home.html')