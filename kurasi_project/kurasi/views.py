from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from .models import Input

# Create your views here.

def home(request):
    context = {
        'inputs': Input.objects.all()
    }
    return render(request, 'kurasi/home.html', context)

class InputListView(ListView): 
    model = Input
    template_name = 'kurasi/home.html'
    context_object_name = 'inputs'
    ordering = ['-date_posted']


class InputDetailView(DetailView):
    model = Input


class InputCreateView(LoginRequiredMixin, CreateView):
    model = Input
    fields = ['nama', 'judul', 'kategori','link','kelas','pelajaran']

    def form_valid(self, form):
        form.instance.nama = self.request.user
        return super().form_valid(form)


class InputUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Input
    fields = ['nama', 'judul', 'kategori', 'link', 'kelas', 'pelajaran']

    def form_valid(self, form):
        form.instance.nama = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        input = self.get_object()
        if self.request.user == input.nama:
            return True
        return False


class InputDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Input
    success_url = '/'
    
    def test_func(self):
        input = self.get_object()
        if self.request.user == input.nama:
            return True
        return False

def about(request):
    return render(request, 'kurasi/about.html', {'judul': 'About'})
