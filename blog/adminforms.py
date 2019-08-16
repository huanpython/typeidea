# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/16 0016  上午 10:49 
# 文件名称   ：adminform.PY
# 开发工具   ：PyCharm
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)