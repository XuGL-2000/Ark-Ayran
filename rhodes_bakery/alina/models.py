from django.db import models


# Create your models here.

class Login(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=18)
    password = models.CharField(verbose_name="密码", max_length=120)

    def __str__(self):
        return self.username
