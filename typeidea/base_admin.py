# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/16 0016  上午 10:49 
# 文件名称   ：base_admin.PY
# 开发工具   ：PyCharm
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)