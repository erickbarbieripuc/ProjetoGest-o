from django.urls import path
from .views import DashboardView, TaskListView, TaskCreateView
from django.views.generic import TemplateView
from .views import KanbanView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='task_new'),
    # path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('projects/', TemplateView.as_view(template_name='core/projects.html'), name='projects'),
    path('project-form/', TemplateView.as_view(template_name='core/project_form.html'), name='project_form'),
    path('project-detail/', TemplateView.as_view(template_name='core/project-detail.html'), name='project_detail'),
    path('kanban/', KanbanView.as_view(), name='kanban'),
    path('assignments/', TemplateView.as_view(template_name='core/assignments.html'), name='assignments'),
    path('deadlines/', TemplateView.as_view(template_name='core/deadlines.html'), name='deadlines'),
    path('reports/', TemplateView.as_view(template_name='core/reports.html'), name='reports'),
    path('teams/', TemplateView.as_view(template_name='core/teams.html'), name='teams'),
    path('chat/', TemplateView.as_view(template_name='core/chat.html'), name='chat'),
    path('profile/', TemplateView.as_view(template_name='core/profile.html'), name='profile'),
    path('project-settings/', TemplateView.as_view(template_name='core/project-settings.html'), name='project_settings'),
    path('help/', TemplateView.as_view(template_name='core/help.html'), name='help'),
]
