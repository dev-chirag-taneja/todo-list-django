from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
  
# Create your views here.
class CustomLoginView(LoginView):
    fields = '__all__'
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True 

    def get_success_url(self):
        return reverse_lazy('todos')

class CustomLogoutView(LogoutView):
     next_page = 'todos' 

class CustomRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('todos')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return self.render_to_response(self.get_context_data())