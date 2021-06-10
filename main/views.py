from django.shortcuts import redirect, render
from .models import Comment, Task, Membership
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
    tasks = request.user.task_set.values()
    friends_tasks = request.user.shared_tasks.all()
    return render(request, 'index.html', {'tasks':tasks,'friends_tasks':friends_tasks})
    
    
@login_required
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('index')
    else:
        form = TaskForm()
        return render(request, 'add_task.html', {'form':form})

@login_required
def delete(request, id):
    Task.objects.get(id = id).delete()
    return redirect('index')

@login_required
def share(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        # share_with = User.objects.get(username = request.POST['username'])
        form = ShareForm(request.POST)
        # if share_with is not None:
        if form.is_valid:
            # print(task, share_with)
            # task.save()
            # task.shared.add(share_with)
            membership = form.save(commit=False)
            membership.task = task
            membership.save()
            
        return redirect('index')
    else:
        form = ShareForm()
        return render(request, 'share.html', {'form':form})

@login_required
def view(request, id):
    
    task = Task.objects.get(id = id)
    try:
        comment_allowed = Membership.objects.get(task = task, user = request.user).status 
    except:
        comment_allowed = True
    print(comment_allowed)
    comments = task.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit = False)
        comment.task = task
        comment.user = request.user
        comment.save()
        return render(request, 'view.html', {'task':task, 'comments':comments, 'form':CommentForm()})
    else:
        form = CommentForm()
        return render(request, 'view.html', {'task':task, 'comments':comments, 'form':form, 'comment_allowed':comment_allowed})
        



