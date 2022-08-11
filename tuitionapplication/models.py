# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actionclosure(models.Model):
    actionclose_inc = models.OneToOneField('Incidentreporting', models.DO_NOTHING, primary_key=True)
    actiondonebyname = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    actiontaken = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    completiondate = models.DateField()
    verify_email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'actionclosure'


class Adduser(models.Model):
    addemp_id = models.IntegerField(primary_key=True)
    addemail = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    addname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    adddepartment = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    addsection = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    addrole = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    designation = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    addtraining = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    addphone = models.DecimalField(max_digits=15, decimal_places=0)
    addpassword = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'adduser'


class Assigninvestigator(models.Model):
    incident = models.OneToOneField('Incidentreporting', models.DO_NOTHING, primary_key=True)
    nameassignedinvestigator = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    emailassignedinvestigator = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'assigninvestigator'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

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
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Finalreport(models.Model):
    reinc = models.OneToOneField('Incidentreporting', models.DO_NOTHING, primary_key=True)
    reinc_type = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    summary = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inv_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inv_id = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    re_date = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    re_time = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    re_loc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inv_vic_name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    injuries = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    fatalities = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    vic_fat_desc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    rca = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    rtc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ca = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cap = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cad = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pa = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pap = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pat = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ma = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    intensity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'finalreport'


class Incidentreporting(models.Model):
    reportingincident_id = models.IntegerField(primary_key=True)
    datereport = models.DateField()
    timereport = models.TimeField()
    reportedby = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    dateincident = models.DateField()
    timeincident = models.TimeField()
    locationincident = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    incidentdesc = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    incidentaction = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    victimname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    victimrole = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    victimemp_id = models.IntegerField()
    victimcon_id = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    assign_inv_email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'incidentreporting'


class Specialanalyzing(models.Model):
    spe_inc = models.OneToOneField(Incidentreporting, models.DO_NOTHING, primary_key=True)
    imm_cause_unsafe_ac = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imm_cause_unsafe_con = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    root_cause_human_fac = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    root_cause_org_fac = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'specialanalyzing'


class Verifyactionclose(models.Model):
    ver_action_close_inc = models.OneToOneField(Incidentreporting, models.DO_NOTHING, primary_key=True)
    inc_closeoropen = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    remarks = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    assigner_mail_final = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'verifyactionclose'


class Whywhyanalyzing(models.Model):
    whyinc = models.OneToOneField(Incidentreporting, models.DO_NOTHING, primary_key=True)
    ps = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    why1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    why2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    why3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    why4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    why5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    rc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'whywhyanalyzing'
