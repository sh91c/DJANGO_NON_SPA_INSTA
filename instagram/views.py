from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from .form import PostForm


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # extract tag name (model.py 참고)
            # 중간 테이블에 insert 되야하기 때문에 post가 저장되고 pk가 있어야함
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, '포스팅을 작성했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'instagram/post_form.html', {
        'form': form
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'instagram/post_detail.html', {
        'post': post
    })


@login_required
def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    return render(request, 'instagram/user_page.html', {
        'page_user': page_user,
        'post_list': post_list,
    })