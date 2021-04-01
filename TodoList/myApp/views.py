from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Task
from . forms import TaskForm,RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.
class home(ListView):
    model = Task
    template_name = 'task.html'

class Detail(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'tasks'

class Create(CreateView):
    model = Task
    form_class = TaskForm
    template_name ='create.html'

class Update(UpdateView):
    model = Task
    form_class = TaskForm
    template_name ='update.html'

class Delete(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('home')
    template_name ='delete.html'
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})