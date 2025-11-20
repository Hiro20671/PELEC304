from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import RegisterForm, EnrollmentForm
from .models import Enrollment

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    form = EnrollmentForm()

    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment submitted successfully!")
            return redirect('home')

    enrollments = Enrollment.objects.all().order_by('-date_created')
    return render(request, 'home.html', {'form': form, 'enrollments': enrollments})


@login_required
def enrollment_edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        messages.success(request, "Enrollment updated successfully!")
        return redirect('home')
    return render(request, 'enrollment_form.html', {'form': form, 'title': 'Edit Enrollment'})

@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        enrollment.delete()
        messages.success(request, "Enrollment deleted successfully!")
        return redirect('home')
    return render(request, 'enrollment_confirm_delete.html', {'enrollment': enrollment})