from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {'form': form})

def success_view(request):
    return redirect('success')
