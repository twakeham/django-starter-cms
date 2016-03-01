import datetime

from django.shortcuts import get_object_or_404, render
from django.utils.timezone import utc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Post


def list_view(request, slug=None):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    post_list = Post.objects.filter(published__lt=now).order_by('-published')

    # category view
    if slug:
        post_list = post_list.filter(categories__slug=slug)
    
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
            
    return render(request, 'post/list.html', {'posts': posts})

def single_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post/single.html', {'post':post})


