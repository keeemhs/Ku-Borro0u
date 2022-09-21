# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    title = models.CharField(primary_key=True, max_length=30)
    regist_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    notice = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    regist_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class User(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    iden_code = models.AutoField(primary_key=True)
    regis_date = models.DateField(blank=True, null=True)
    borrow_code = models.IntegerField(blank=True, null=True)
    regist_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('iden_code', 'email'),)