
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	STATUS_CHOICES = [
		('novo', 'Novo'),
		('andamento', 'Em andamento'),
		('concluido', 'Concluído'),
	]
	name = models.CharField(max_length=100)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='novo')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Task(models.Model):
	STATUS_CHOICES = [
		('todo', 'A fazer'),
		('doing', 'Fazendo'),
		('done', 'Feito'),
	]
	PRIORITY_CHOICES = [
		('baixa', 'Baixa'),
		('media', 'Média'),
		('alta', 'Alta'),
	]
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='media')
	due_date = models.DateField()
	assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

# Create your models here.
