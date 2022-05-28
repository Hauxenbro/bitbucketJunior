from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.http import HttpResponseNotFound
from .models import Workers
from .forms import UserLoginForm, UserRegisterForm, AddWorkerForm


# Create your views here.

def delete_user(request, worker_id):
    try:
        worker = Workers.objects.get(pk=worker_id)
        worker.delete()
        return redirect('all_workers')
    except Workers.DoesNotExist:
        return HttpResponseNotFound("<h2>Worker is not found</h2>")


def edit_worker(request, worker_id):
    try:
        worker = Workers.objects.get(pk=worker_id)
        if request.method == 'POST':
            form = AddWorkerForm(data=request.POST)
            if form.is_valid():
                worker.delete()
                form.save()
                return redirect('all_workers')
        else:
            form = AddWorkerForm(data={'name':worker.name, 'working_place':worker.working_place,
                                       'salary':worker.salary, 'parent':worker.parent, 'photo':worker.photo})
        return render(request, 'workers_here/edit_worker.html', {'form': form})
    except Workers.DoesNotExist:
        return HttpResponseNotFound('<h2>Worker is not found</h2>')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_workers')
    else:
        form = UserRegisterForm()
    return render(request, 'workers_here/register_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_workers')
    else:
        form = UserLoginForm()
    return render(request, 'workers_here/login_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('all_workers')


class WorkerAddition(CreateView):
    form_class = AddWorkerForm
    template_name = 'workers_here/add_worker.html'


class WorkerDetailed(DetailView):
    model = Workers
    pk_url_kwarg = 'worker_id'
    template_name = 'workers_here/worker_detailed.html'
    context_object_name = 'worker'


class WorkerFull(ListView):
    model = Workers
    template_name = 'workers_here/workers.html'
    context_object_name = 'Workers'

    def get_queryset(self):
        return Workers.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkerSortedName(ListView):
    model = Workers
    template_name = 'workers_here/workers_name.html'
    context_object_name = 'Workers'

    def get_queryset(self):
        return Workers.objects.order_by('-' + self.request.GET.get('knopka')).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkerSearch(ListView):
    model = Workers
    template_name = 'workers_here/search.html'
    context_object_name = 'workers'

    def get_queryset(self):
        return Workers.objects.filter(name__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
