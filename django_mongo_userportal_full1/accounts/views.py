from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserProfile.objects.get(username=username, password=password)
            if user.role == 'Patient':
                return render(request, 'dashboard_patient.html', {'user': user})
            else:
                return render(request, 'dashboard_doctor.html', {'user': user})
        except UserProfile.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
