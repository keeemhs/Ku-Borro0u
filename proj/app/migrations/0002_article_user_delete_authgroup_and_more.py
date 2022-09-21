# Generated by Django 4.1 on 2022-09-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('regist_date', models.DateField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('notice', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('regist_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('iden_code', models.AutoField(primary_key=True, serialize=False)),
                ('regis_date', models.DateField(blank=True, null=True)),
                ('borrow_code', models.IntegerField(blank=True, null=True)),
                ('regist_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
