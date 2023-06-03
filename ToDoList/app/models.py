from django.db import models

# Create your models here.

class Todolist(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField(max_length=100)
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(null=True, default=None) #생성시간
    rewrited_at=models.DateTimeField(null=True, default=None) #수정시간
    due=models.DateField(null=True, default=None) #마감일


    def __str__(self):
        return self.title