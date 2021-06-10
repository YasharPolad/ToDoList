from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Task(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    shared = models.ManyToManyField(User, through = 'Membership', related_name='shared_tasks')

    def __str__(self):
        return f"{self.name}-{self.user.username}"


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.task}"

class Membership(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
  

    def __str__(self):
        return f"{self.task.name}-{self.user.username}-{self.status}"

#yashar.membership_set.values('status').get(id=1)['status']
