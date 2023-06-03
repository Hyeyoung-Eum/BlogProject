from django.db import models

# Create your models here.

class Todolist(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField(max_length=100)
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True) #생성시간
    due=models.DateTimeField(null=True) #마감시간


    def __str__(self):
        return self.title