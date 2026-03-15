from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bugs')
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.description}"