from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Job
from .forms import JobForm, ApplicationForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jobs/jobs_list.html')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def jobs_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'jobs/jobs_list.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {'job': job}
    return render(request, 'jobs/job_detail.html', context)


def job_apply(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=job_id)
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.job = job
            application.save()
            return redirect('jobs:job_detail', job_id=job_id)
    else:
        application_form = ApplicationForm()
    context = {'form': application_form}
    return render(request, 'jobs/job_apply.html', context)


def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:jobs_list')
    else:
        form = JobForm()
    context = {'form': form}
    return render(request, 'jobs/create_job.html', context)


def update_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_detail', job_id=job_id)
    else:
        form = JobForm(instance=job)
    context = {'form': form, 'job': job}
    return render(request, 'jobs/job_update.html', context)


def job_delete(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:jobs_list')
    context = {'job': job}
    return render(request, 'jobs/job_delete.html', context)


def job_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        jobs = Job.objects.filter(title__icontains=search_query)
        context = {'jobs': jobs}
        return render(request, 'jobs/search_results.html', context)
    else:
        return render(request, 'jobs/job_search_form.html')


def search_results(request):
    search_query = request.GET.get('q')
    if search_query:
        jobs = Job.objects.filter(title__icontains=search_query)
    else:
        jobs = Job.objects.none()
    context = {'jobs': jobs, 'search_query': search_query}
    return render(request, 'jobs/search_results.html', context)

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
