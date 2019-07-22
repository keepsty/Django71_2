# Create your views here.
from django.shortcuts import render

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django71_2.settings')
import django

django.setup()

from app01 import models
from utils.page_list import PageList


def books(request):
    page_num = request.GET.get('page')
    total_count = models.Book.objects.all().count()
    page_obj = PageList(data_num=10, page_num=page_num, url_prefix='books', total_count=total_count, page_max_len=7)

    print(page_obj.start(), page_obj.end())
    ret = models.Book.objects.all()[page_obj.start():page_obj.end()]
    html_str = page_obj.page_html()
    # data_start = (page_num - 1) * 10
    # data_end = (page_num) * 10
    # ret = models.Book.objects.all()[data_start:data_end]
    # total_page, m = divmod(total_count, data_num)
    #
    # try:
    #     # 当输入非法的page_num = abc 时，跳转到首页
    #     page_num = int(page_num)
    #
    #     #     如果当前页大于总页码，设置page_num = 最后一页
    #     if page_num > total_page:
    #         page_num = total_page
    #
    # except Exception as e:
    #     page_num = 1
    #
    # if m:
    #     total_page += 1
    # html_str_list = []
    # # 设置页码总数为7
    # page_max_len = 7
    # # 开始页码，结束页码
    # start_page = page_num - int(page_max_len / 2)
    # end_page = page_num + int(page_max_len / 2)
    # if start_page < 1:
    #     start_page = 1
    #     end_page = page_max_len
    #
    # if end_page >= total_page:
    #     end_page = total_page
    #     start_page = total_page - page_max_len + 1
    # # 循环方式把样式传输给html
    #
    # html_str_list.append('<li><a href="/books/?page=1">首页</a></li>')
    # # 前一页：当前页 <=1 时，前一页=1，否则 前一页 = page_num-1
    # if page_num <= 1:
    #     html_str_list.append(
    #         '<li><a href="/books/?page=1" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     html_str_list.append(
    #         '<li><a href="/books/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
    #             page_num - 1))
    #
    # for i in range(start_page, end_page + 1):
    #     tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
    #     html_str_list.append(tmp)
    #
    # # 后一页：当前页 <=total_page 时，前一页=total_page，否则 前一页 = page_num-1
    # if page_num >= total_page:
    #     html_str_list.append(
    #         '<li class="disable"><a href="/books/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
    #             total_page))
    # else:
    #     html_str_list.append(
    #         '<li><a href="/books/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
    #             page_num + 1))
    #
    # html_str_list.append('<li><a href="/books/?page={}">尾页</a></li>'.format(total_page))
    #
    # page_nav = ''.join(html_str_list)

    #
    return render(request, 'page.html', {"total_count": total_count, 'ret': ret, "page_nav": html_str})


def dept(request):
    page_num = request.GET.get('page')
    total_count = models.Dept.objects.all().count()
    page_obj = PageList(data_num=10, page_num=page_num, url_prefix='dept', total_count=total_count, page_max_len=7)

    print(page_obj.start(), page_obj.end())
    ret = models.Dept.objects.all()[page_obj.start():page_obj.end()]
    # print(page_obj.page_nav)
    html_str = page_obj.page_html()
    # data_start = (page_num - 1) * 10
    # data_end = (page_num) * 10
    # ret = models.Book.objects.all()[data_start:data_end]
    # total_page, m = divmod(total_count, data_num)
    #
    # try:
    #     # 当输入非法的page_num = abc 时，跳转到首页
    #     page_num = int(page_num)
    #
    #     #     如果当前页大于总页码，设置page_num = 最后一页
    #     if page_num > total_page:
    #         page_num = total_page
    #
    # except Exception as e:
    #     page_num = 1
    #
    # if m:
    #     total_page += 1
    # html_str_list = []
    # # 设置页码总数为7
    # page_max_len = 7
    # # 开始页码，结束页码
    # start_page = page_num - int(page_max_len / 2)
    # end_page = page_num + int(page_max_len / 2)
    # if start_page < 1:
    #     start_page = 1
    #     end_page = page_max_len
    #
    # if end_page >= total_page:
    #     end_page = total_page
    #     start_page = total_page - page_max_len + 1
    # # 循环方式把样式传输给html
    #
    # html_str_list.append('<li><a href="/books/?page=1">首页</a></li>')
    # # 前一页：当前页 <=1 时，前一页=1，否则 前一页 = page_num-1
    # if page_num <= 1:
    #     html_str_list.append(
    #         '<li><a href="/books/?page=1" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     html_str_list.append(
    #         '<li><a href="/books/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
    #             page_num - 1))
    #
    # for i in range(start_page, end_page + 1):
    #     tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
    #     html_str_list.append(tmp)
    #
    # # 后一页：当前页 <=total_page 时，前一页=total_page，否则 前一页 = page_num-1
    # if page_num >= total_page:
    #     html_str_list.append(
    #         '<li class="disable"><a href="/books/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
    #             total_page))
    # else:
    #     html_str_list.append(
    #         '<li><a href="/books/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
    #             page_num + 1))
    #
    # html_str_list.append('<li><a href="/books/?page={}">尾页</a></li>'.format(total_page))
    #
    # page_nav = ''.join(html_str_list)

    #
    return render(request, 'dept_page.html', {"total_count": total_count, 'ret': ret, "page_nav": html_str})
