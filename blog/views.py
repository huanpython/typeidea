from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from blog.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    categoty = None


    if tag_id:
        post_list, tag=Post.get_by_tag(tag_id)
    elif category_id:
        post_list, categoty=Post.get_by_categoty(category_id)
    else:
        post_list=Post.latest_posts()

    content = {
        'category': categoty,
        'tag': tag,
        'post_list': post_list,
        'sidebars':SideBar.get_all(),
    }

    content.update(Category.get_navs())

    return render(request, 'blog/list.html',context=content)





def post_detail(request, post_id=None):

    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        post=None


    content={
        'post':post,
        'sidebars': SideBar.get_all(),
    }

    content.update(Category.get_navs())
    return render(request,'blog/detail.html', context={'post':'post'})
