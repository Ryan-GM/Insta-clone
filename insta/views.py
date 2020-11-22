from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Profile,Comment,Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .forms import PostForm,UpdateUserForm,CommentForm,SignUpForm,UpdateUserProfileForm
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.

@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'insta/index.html', params)