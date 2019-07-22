#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-06-12 10:35
# from django.shortcuts import render, HttpResponse
# import os
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django71_2.settings')
# import django
#
# django.setup()
# from app01 import models


class PageList(object):
    def __init__(self, data_num, page_num, url_prefix, total_count, page_max_len):
        '''

        :param data_num: 一页多少条数据
        :param page_num: 当前页码数
        :param url_prefix: 页码数据链接
        :param total_count: 数据总行数
        :param page_max_len: 分页最长长度
        '''
        self.data_num = data_num
        self.page_num = page_num
        self.total_count = total_count
        self.page_max_len = page_max_len
        self.url_prefix = url_prefix
        self.page_total, m = divmod(self.total_count, self.data_num)

        if m:
            self.page_total += 1
        try:
            # 当输入非法的page_num = abc 时，跳转到首页
            self.page_num = int(self.page_num)

            #     如果当前页大于总页码，设置page_num = 最后一页
            if self.page_num > self.page_total:
                self.page_num = self.page_total

        except Exception as e:
            self.page_num = 1

        self.data_start = (self.page_num - 1) * self.data_num
        self.data_end = self.page_num * self.data_num
        # 设置页码总数为7
        # 开始页码，结束页码

        # 如果总页码小于 页码总长度，把 page_total 赋值给page_max_len
        if self.page_total <= self.page_max_len:
            self.page_max_len = self.page_total

        self.page_start = self.page_num - int(page_max_len / 2)
        self.page_end = self.page_num + int(page_max_len / 2)
        if self.page_start <= 1:
            self.page_start = 1
            self.page_end = self.page_max_len

        if self.page_end >= self.page_total:
            self.page_end = self.page_total
            self.page_start = self.page_total - self.page_max_len + 1

    def start(self):
        return self.data_start

    def end(self):
        return self.data_end

    def page_html(self):
        # 循环方式把样式传输给html
        html_str_list = []
        html_str_list.append('<li><a href="/{}/?page=1">首页</a></li>'.format(self.url_prefix))
        # 前一页：当前页 <=1 时，前一页=1，否则 前一页 = page_num-1
        if self.page_num <= 1:
            html_str_list.append(
                '<li><a href="/{}/?page=1" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.url_prefix))
        else:
            html_str_list.append(
                '<li><a href="/{0}/?page={1}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.url_prefix, self.page_num - 1))

        for i in range(self.page_start, self.page_end + 1):
            if i == self.page_num:
                tmp = '<li class="active"><a href="/{0}/?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="/{0}/?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            html_str_list.append(tmp)

        # 后一页：当前页 <=page_total 时，前一页=page_total，否则 前一页 = page_num-1
        if self.page_num >= self.page_total:
            html_str_list.append(
                '<li class="disable"><a href="/{0}/?page={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix,
                    self.page_total))
        else:
            html_str_list.append(
                '<li><a href="/{0}/?page={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix,
                    self.page_num + 1))

        html_str_list.append('<li><a href="/{0}/?page={1}">尾页</a></li>'.format(self.url_prefix, self.page_total))
        page_nav = ''.join(html_str_list)
        return page_nav
