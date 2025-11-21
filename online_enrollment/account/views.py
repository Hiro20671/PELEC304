from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EnrollmentForm, SubjectForm
from .models import Enrollment, Subject


# -----------------------------
# REGISTER
# -----------------------------
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'register.html', {'form': form})


# -----------------------------
# LOGIN
# -----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


# -----------------------------
# LOGOUT
# -----------------------------
def logout_view(request):
    logout(request)
    return redirect('login')


# -----------------------------
# HOME / DASHBOARD
# -----------------------------
@login_required
def home_view(request):
    enrollment_form = EnrollmentForm()
    subject_form = SubjectForm()
    subjects = Subject.objects.all()
    enrollments = Enrollment.objects.all().order_by('-date_created')

    # Handle form submissions
    if request.method == "POST":
        if 'enrollment_submit' in request.POST:
            enrollment_form = EnrollmentForm(request.POST)
            if enrollment_form.is_valid():
                enrollment_form.save()
                messages.success(request, "Enrollment submitted successfully!")
                return redirect('home')
        elif 'subject_submit' in request.POST:
            subject_form = SubjectForm(request.POST)
            if subject_form.is_valid():
                subject_form.save()
                messages.success(request, "Subject added successfully!")
                return redirect('home')

    context = {
        'enrollment_form': enrollment_form,  # for Enrollment form
        'subject_form': subject_form,        # for Subjects form
        'subjects': subjects,                # list of subjects
        'enrollments': enrollments,          # list of enrolled students
    }
    return render(request, 'home.html', context)


# -----------------------------
# ENROLLMENT EDIT
# -----------------------------
@login_required
def enrollment_edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    form = EnrollmentForm(request.POST or None, instance=enrollment)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment updated successfully!")
            return redirect('home')

    return render(request, 'enrollment_form.html', {
        'form': form,
        'title': "Edit Enrollment"
    })

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')


# -----------------------------
# ENROLLMENT DELETE
# -----------------------------
@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == "POST":
        enrollment.delete()
        messages.success(request, "Enrollment deleted successfully!")
        return redirect('home')

    return render(request, 'enrollment_confirm_delete.html', {
        'enrollment': enrollment
    })


# -----------------------------
# SUBJECT ADD
# -----------------------------
@login_required
def subject_add(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject added successfully!")
            return redirect('home')
    else:
        form = SubjectForm()

    return render(request, 'subject_form.html', {
        'form': form,
        'title': "Add Subject"
    })


# -----------------------------
# SUBJECT EDIT
# -----------------------------
@login_required
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully!")
            return redirect('home')

    return render(request, 'subject_form.html', {
        'form': form,
        'title': "Edit Subject"
    })


# -----------------------------
# SUBJECT DELETE
# -----------------------------
@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == "POST":
        subject.delete()
        messages.success(request, "Subject deleted successfully!")
        return redirect('home')

    return render(request, 'subject_confirm_delete.html', {
        'subject': subject
    })

