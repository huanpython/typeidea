from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def post_list(request,category_id=None,tag_id=None):
#     content='post_list category_id={category_id}, tag_id={tag_id}'.format(
#         category_id=category_id,
#         tag_id=tag_id,
#     )
#
#     return HttpResponse(content)
from blog.models import Tag, Post, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    categoty = None


    if tag_id:
        try:
            tag=Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list=[]
        else:
            post_list=tag.post_set.filter(status=Post.STATUS_NORMAL)

    else:
        post_list=Post.objects.filter(status=Post.STATUS_NORMAL)

        if category_id:
            try:
                categoty=Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                categoty=None

        else:
            post_list=post_list.filter(category_id=category_id)

    content = {
        'category': categoty,
        'tag': tag,
        'post_list': post_list,
    }

    return render(request, 'blog/list.html',context=content)





def post_detail(request, post_id=None):

    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        post=None

    return render(request,'blog/detail.html', context={'post':'post'})
