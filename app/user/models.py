from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    name:
    使用者模型

    fields:
    email: email
    username: 姓名
    unit: 單位
    contact: 聯絡方式
    """
    email = models.EmailField(unique=True, max_length=255, null=False, blank=False)
    username = models.CharField(verbose_name="姓名",  max_length=255, null=False, blank=False)
    unit = models.CharField(verbose_name="單位", max_length=100, null=True, blank=True)
    contact = models.CharField(verbose_name="聯絡方式", max_length=100, null=True, blank=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'  # 使用信箱當登入帳號
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
