from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from postcrud.models import Post
from commentcrud.models import Comment

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html', {'form':form, 'post':post})

def commentupdate(request, post_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        updateform = CommentForm(request.POST, instance = comment)
        if updateform.is_valid():
            updateform.save()
            return redirect('postshow', post_id)
    return render(request, 'commentedit.html', {'form':form})

def commentdelete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('postshow', post_id)