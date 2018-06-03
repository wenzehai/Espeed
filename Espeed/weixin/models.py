# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django_mysql.models import SetTextField


# Create your models here.

class UserProfileBase(models.Model):
    #  "改造用户身份认证所需表结构"
    fromUser = models.OneToOneField(User)
    nickName = models.CharField(max_length=30)		# 微信昵称
    openId = models.CharField(max_length=50)        # Openid
    Sex = models.IntegerField(default=True)			# 微信标识的性别
    userName = models.CharField(max_length=30)			# 用户真实名称，注册时输入的
    country = models.CharField(max_length=30)			# 国家
    province = models.CharField(max_length=30)		# 省份
    city = models.CharField(max_length=30)			# 城市
    phonenum = models.CharField(max_length=20)				# 电话
    avatarAddr = models.URLField()						# 头像
    Role = models.IntegerField(default=True)	    # 身份
    Location_lati = models.FloatField(null=True)     # 定位
    Location_longi = models.FloatField(null=True)  # 定位
    Score = models.IntegerField(default=5)       # 评分
    ScoreCount = models.IntegerField(default=True)	# 评价人数
    Jobs = SetTextField(
        base_field=models.CharField(max_length=32),
    )           # 工种类型
    online = models.BooleanField(default=False)     # 是否在线
    createTime = models.DateTimeField(auto_now_add=True)				# 注册时间
    last_login = models.DateField(default=None)			# 最后访问时间
    publishTime = models.CharField(max_length=20, null=True)

class UserVisible(models.Model):
    transation_no = models.CharField(default=None, max_length=50)
    paysign = models.CharField(default=None, max_length=50)
    user_payed = models.CharField(max_length=50)  # Openid
    user_visible = models.CharField(max_length=50)  # Openid
    pay_status = models.CharField(default='prepay', max_length=50)
    request_time = models.CharField(max_length=20, null=True,blank=True,default=None)
    payed_time = models.CharField(max_length=20, null=True,blank=True, default=None)

class Jobcates(models.Model):
    jobcate = models.CharField(max_length=32)

class transations(models.Model):
    transations_user = models.CharField(max_length=50)

class verify_code_request(models.Model):
    request_ip = models.CharField(max_length=50)
    request_phonenum = models.CharField(max_length=50)
    request_time = models.CharField(max_length=50)

class send_template(models.Model):
    useropenid = models.DateField(default=None)