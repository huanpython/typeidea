# -*- coding: utf-8 -*-
# @Time : 2019/8/16 0016 1:52
# @Author : huanfuan
# @FileName: custom_site.py
# @Software: PyCharm
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
