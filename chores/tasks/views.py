from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, TaskCategory
from django.shortcuts import redirect
from django.utils import timezone
from .forms import TaskForm, TaskCategoryForm
from .mixins import TaskOwnerMixin 

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

class TaskDetailView(TaskOwnerMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskDeleteView(TaskOwnerMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")


def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = 'completed'
    task.completed_at = timezone.now()
    task.progress = 100
    task.save()
    return redirect('tasks:task_list')


class TaskCategoryListView(ListView):
    model = TaskCategory
    template_name = "tasks/task_category_list.html"
    context_object_name = "task_categories"

    def get_queryset(self):
        return TaskCategory.objects.filter(user = self.request.user)
    

class TaskCategoryDetailView(TaskOwnerMixin, DetailView):
    model = TaskCategory
    template_name = "tasks/task_category_detail.html"


class TaskCategoryCreateView(CreateView):
    model = TaskCategory
    form_class = TaskCategoryForm
    template_name = "tasks/task_category_form.html"
    success_url = reverse_lazy("tasks:task_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskCategoryUpdateView(TaskOwnerMixin, UpdateView):
    model = TaskCategory
    form_class = TaskCategoryForm
    template_name = "tasks/task_category_form.html"
    success_url = reverse_lazy("tasks:task_category_list")


class TaskCategoryDeleteView(TaskOwnerMixin, DeleteView):
    model = TaskCategory
    template_name = "tasks/task_category_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_category_list")







    



   
