#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-06-11 11:21


import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django71_2.settings')
    import django

    django.setup()

    # from app01 import models

    from app01 import models

    # obj = [models.Book(title='天通苑{}'.format(i+100)) for i in range(1000)]
    # models.Book.objects.bulk_create(obj, 100)

    obj = [models.Dept(dept_name='华强北{}'.format(i)) for i in range(12)]
    models.Dept.objects.bulk_create(obj, 100)
    print(1)
