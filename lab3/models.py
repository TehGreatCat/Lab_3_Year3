# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargodepot(models.Model):
    cargo_id = models.BigAutoField(primary_key=True)
    height = models.IntegerField()
    volume = models.BigIntegerField(blank=True, null=True)
    numberofloaders = models.IntegerField(blank=True, null=True)
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    class Meta:
        managed = False
        db_table = 'cargodepot'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Flight(models.Model):
    flight_id = models.BigAutoField(primary_key=True)
    passengers = models.IntegerField(blank=True, null=True)
    plane = models.ForeignKey('Plane', models.DO_NOTHING, db_column='plane', blank=True, null=True)
    timeofarrival = models.TimeField(blank=True, null=True)
    gates = models.ForeignKey('Gates', models.DO_NOTHING, db_column='gates')
    type = models.CharField(max_length=255, blank=True, null=True)
    runway = models.ForeignKey('Runway', models.DO_NOTHING, db_column='runway')
    timeofdeparture = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight'


class Gates(models.Model):
    gates_id = models.BigAutoField(primary_key=True)
    throughput = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    class Meta:
        managed = False
        db_table = 'gates'


class Plane(models.Model):
    plane_id = models.CharField(primary_key=True, max_length=30)
    seats = models.BigIntegerField(blank=True, null=True)
    fuelweight = models.BigIntegerField(blank=True, null=True)
    wingspan = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plane'


class Runway(models.Model):
    runway_id = models.BigAutoField(primary_key=True)
    length = models.IntegerField(blank=True, null=True)
    weightallowed = models.IntegerField(blank=True, null=True)
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    class Meta:
        managed = False
        db_table = 'runway'


class Terminal(models.Model):
    terminal_id = models.BigAutoField(primary_key=True)
    passengertraffic = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    radarrange = models.BigIntegerField(blank=True, null=True)
    callsign = models.CharField(db_column='Callsign', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terminal'
