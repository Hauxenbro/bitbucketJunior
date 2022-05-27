from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workers

# Create your views here.

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

    def get_context_data(self, *, object_list = None, **kwargs):
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
        return Workers.objects.filter(name__icontains = self.request.GET.get('s'))

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
