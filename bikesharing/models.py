# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BikeAttribute(models.Model):
    bike_id = models.AutoField(primary_key=True)
    bike_state = models.ForeignKey('BikeState', models.DO_NOTHING, db_column='bike_state')
    bike_stationx = models.FloatField()
    bike_stationy = models.FloatField()
    bike_pointstate = models.IntegerField()
    bike_pointnum = models.ForeignKey('BikePoint', models.DO_NOTHING, db_column='bike_pointnum')

    class Meta:
        managed = False
        db_table = 'bike_attribute'


class BikeFixed(models.Model):
    fixed_id = models.AutoField(primary_key=True)
    fixed_time = models.DateTimeField()
    fixed_bike = models.ForeignKey(BikeAttribute, models.DO_NOTHING)
    fixed_operator = models.ForeignKey('UserReg', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bike_fixed'


class BikePoint(models.Model):
    point_id = models.AutoField(primary_key=True)
    point_name = models.CharField(max_length=45)
    point_startx = models.IntegerField()
    point_starty = models.IntegerField()
    point_endx = models.IntegerField()
    point_endy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bike_point'


class BikeRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    route_bike = models.ForeignKey(BikeAttribute, models.DO_NOTHING)
    route_starttime = models.DateTimeField()
    route_endtime = models.DateTimeField()
    route_price = models.IntegerField()
    route_bike_state = models.ForeignKey('BikeState', models.DO_NOTHING, db_column='route_bike_state')
    route_startx = models.IntegerField()
    route_starty = models.IntegerField()
    route_endx = models.IntegerField()
    route_endy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bike_route'


class BikeState(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'bike_state'


class BikeUsed(models.Model):
    used_id = models.AutoField(primary_key=True)
    used_time = models.DateTimeField()
    used_bike = models.ForeignKey(BikeAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bike_used'


class UserReg(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_password = models.CharField(max_length=45)
    user_perm = models.ForeignKey('UserRole', models.DO_NOTHING, db_column='user_perm')

    class Meta:
        managed = False
        db_table = 'user_reg'


class UserRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_role'
