from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin   

from .models import Todo

# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'main/todos.html'

    # Specific User Todo's
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['todos'] = context['todos'].filter(user=self.request.user)
            context['count'] = context['todos'].filter(complete=False).count()

        else:
            context['todos'] = None

        # Search Todo's
        q = self.request.GET.get('q') 
        if q:
            context['todos'] = context['todos'].filter(title__icontains=q)
            context['q'] = q

        return context

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'main/todo.html'

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todos')
    template_name_suffix = '_form'

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'main/todo_delete.html'
    success_url = reverse_lazy('todos')
