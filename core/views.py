
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, Task
from .forms import TaskForm

class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'core/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['total_projects'] = Project.objects.count()
		context['open_tasks'] = Task.objects.exclude(status='done').count()
		context['latest_tasks'] = Task.objects.order_by('-updated_at')[:5]
		return context

class TaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'core/tasks_list.html'
	context_object_name = 'tasks'
	ordering = ['-updated_at']

class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskForm
	template_name = 'core/task_form.html'
	success_url = reverse_lazy('tasks')


class KanbanView(LoginRequiredMixin, View):
	template_name = 'core/kanban.html'

	def get(self, request):
		tasks = Task.objects.select_related('assignee').all()
		columns = {
			'backlog': tasks.filter(status='todo'),
			'doing': tasks.filter(status='doing'),
			'review': tasks.filter(status='doing'), # ajuste conforme status real
			'done': tasks.filter(status='done'),
		}
		return render(request, self.template_name, {
			'columns': columns,
			'tasks': tasks,
		})

# Create your views here.
