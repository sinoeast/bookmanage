#!/usr/bin/python3
# -*- coding:utf-8 -*-
""""
  @Author: 蓝天
  @Email: lantian27294@hundsun.com
  @Time: 2022/7/28 16:04
  @File: models_test.py
"""
from django.test import TestCase

# Create your tests here.


from book.models import BookInfo, PeopleInfo

# ##################################################新增数据
# 方式一实例化对象 调用save()
book = BookInfo(
    name='猫在想什么',
    pub_date='2010-1-1'
)
book.save()

# 方式二用objects管理器对象
BookInfo.objects.create(
    name='狗在想什么',
    pub_date='2010-1-1'
)

# ##################################################修改数据
# 方式一实例化对象 调用save()
book = BookInfo.objects.get(name='狗在想什么')
book.pub_date = '1000-1-1'
book.save()

# 方式二用objects管理器对象直接修改
BookInfo.objects.filter(name='猫在想什么').update(
    readcount=20,
    pub_date='2222-1-1'
)

# ##################################################删除数据
# 方式一实例化对象 调用delete()
book = BookInfo.objects.get(name='狗在想什么')
book.delete()

# 方式二用objects管理器对象直接修改
BookInfo.objects.filter(name='猫在想什么').delete()

# ##################################################查询数据
# 单一查询 返回一个对象 找不到产生异常
book: BookInfo = BookInfo.objects.get(id=1)
try:
    # BookInfo.objects.get(id=1111)
    BookInfo.objects.get(is_delete=0)
except BookInfo.DoesNotExist:
    print("查询不到")
except BookInfo.MultipleObjectsReturned:
    print("返回不止一个对象")

# 查询所有 返回列表对象
books: list[BookInfo] = BookInfo.objects.all()

# 计数 返回int
bookcount: int = BookInfo.objects.count()

# 筛选查询 返回列表对象
books: list[BookInfo] = BookInfo.objects.filter(is_delete=0)

# 排除符合条件的对象
books: list[BookInfo] = BookInfo.objects.exclude(id=1)

# ##################################################过滤条件的表达语法如下：QuerySet查询API
# 属性名称__比较运算符=值
# 属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线
# 查询编号为1的图书
BookInfo.objects.filter(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 3, 5))
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gte='1980-1-1')

# ##################################################F对象 （主要用于模型类的 A 字段属性与 B 字段属性两者的比较）
from django.db.models import F, Q

# 阅读量是评论量两倍的图书
BookInfo.objects.filter(readcount__gte=F("commentcount") * 2)

# ##################################################Q对象（应用于包含逻辑运算的复杂查询）
# 获取id大于3且阅读量大于40的书
BookInfo.objects.filter(id__gt=3, readcount__gt=40)
BookInfo.objects.filter(Q(id__gt=3) & Q(readcount__gt=30))
# 获取id大于3或阅读量大于40的书
BookInfo.objects.filter(Q(id__gt=3) | Q(readcount__gt=30))
# 获取id不是3的书
BookInfo.objects.filter(~Q(id=3))

# ##################################################聚合韩叔叔 SUM，COUNT，AVG，MIN，MAX。。
from django.db.models import Sum

# 计算阅读总量
BookInfo.objects.aggregate(Sum("readcount"))

# ##################################################排序
# 对阅读量进行降序排序
BookInfo.objects.order_by('-readcount')
BookInfo.objects.order_by('readcount')

# ##################################################关联查询
#主表书籍 从表人物
# 查询书籍是1的任人物信息 使用从表_set获取对象
book: BookInfo = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# 查询人物是1的书籍信息 使用外键获取对象
p: PeopleInfo = PeopleInfo.objects.get(id=1)
p.book: BookInfo
p.book.name: str
# ##################################################关联查询筛选
#从表__字段名__条件
BookInfo.objects.filter(peopleinfo__name__contains='郭')
#外键__字段名__条件
PeopleInfo.objects.filter(book__name__contains='射')




