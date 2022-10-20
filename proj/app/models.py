from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    regist_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    notice = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)    
    categorie = models.CharField(max_length=45, blank=True, null=True)   
    being_rented = models.CharField(max_length=45, blank=True, null=True)
    ident = models.AutoField(primary_key=True)
    test = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    email = models.CharField(max_length=254)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.CharField(max_length=10)
    phone = models.CharField(max_length=45, blank=True, null=True)
    major = models.CharField(max_length=45, blank=True, null=True)
    undergrad = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contact(models.Model):
    title = models.CharField(primary_key=True, max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=300, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    regis_date = models.DateField(blank=True, null=True)
    borrow_code = models.IntegerField(blank=True, null=True)
    regist_code = models.IntegerField(blank=True, null=True)
    major = models.CharField(max_length=45, blank=True, null=True)
    undergrad = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class Photo(models.Model):
    images = models.CharField(max_length=45, blank=True, null=True)
    # image = models.FileField(upload_to='images/')
    username = models.CharField(max_length=45, blank=True, null=True)
    ident = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'photo'


# image = models.ImageField(upload_to='images/')