# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminlogins(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    registration_id = models.CharField(max_length=500, blank=True, null=True)
    user_image = models.CharField(max_length=500, blank=True, null=True)
    user_status = models.CharField(max_length=5)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminlogins'


class AlldataDatetime(models.Model):
    survey_id = models.IntegerField()
    datadate_id = models.AutoField(primary_key=True)
    call_status = models.IntegerField(blank=True, null=True)
    first_intrested = models.IntegerField(blank=True, null=True)
    hundred_percent_date = models.CharField(max_length=25, blank=True, null=True)
    seventyfive_percent_date = models.CharField(max_length=25, blank=True, null=True)
    fifty_percent_date = models.CharField(max_length=25, blank=True, null=True)
    twentyfive_percent_date = models.CharField(max_length=25, blank=True, null=True)
    ten_percent_date = models.CharField(max_length=25, blank=True, null=True)
    zero_percent_date = models.CharField(max_length=25, blank=True, null=True)
    bda_reject_date = models.CharField(max_length=25, blank=True, null=True)
    transfer_data = models.IntegerField(blank=True, null=True)
    bda_call_done_date = models.DateTimeField(blank=True, null=True)
    bda_waiting_date = models.CharField(max_length=25, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    bda_call_id = models.IntegerField(blank=True, null=True)
    admin_bda_id = models.IntegerField(blank=True, null=True)
    bda_call_not_done_date = models.DateTimeField(blank=True, null=True)
    bda_call_not_attend_date = models.DateTimeField(blank=True, null=True)
    bda_call_wrong_num_date = models.DateTimeField(blank=True, null=True)
    bda_call_switchstop_date = models.DateTimeField(blank=True, null=True)
    bda_call_evening_date = models.DateTimeField(blank=True, null=True)
    sry_waiting_payment_date = models.DateTimeField(blank=True, null=True)
    sry_payment_date = models.DateTimeField(blank=True, null=True)
    sry_reject_date = models.DateTimeField(blank=True, null=True)
    sry_pendding_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alldata_datetime'


class AndroidapiActivationCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=60)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    price = models.CharField(max_length=25, blank=True, null=True)
    validdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'androidapi_activation_code'


class Appversion(models.Model):
    version = models.CharField(max_length=20)
    link = models.TextField()
    type = models.IntegerField()
    changes = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appversion'


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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Bdainfo(models.Model):
    bdainfo_id = models.AutoField(primary_key=True)
    bdalogin_id = models.IntegerField()
    selectsurveyuser_id = models.IntegerField(blank=True, null=True)
    assign_state = models.IntegerField(blank=True, null=True)
    assign_dist = models.IntegerField(blank=True, null=True)
    assign_block = models.IntegerField(blank=True, null=True)
    assign_village = models.IntegerField(blank=True, null=True)
    bdainfo_current_address = models.CharField(max_length=200, blank=True, null=True)
    bdainfo_present_address = models.CharField(max_length=200, blank=True, null=True)
    bdainfo_adhar_number = models.CharField(max_length=15, blank=True, null=True)
    bdainfo_adhar_front_image = models.CharField(max_length=500, blank=True, null=True)
    bdainfo_adhar_back_image = models.CharField(max_length=500, blank=True, null=True)
    bdainfo_highqualification = models.CharField(max_length=50, blank=True, null=True)
    bdainfo_bankname = models.CharField(max_length=50, blank=True, null=True)
    bdainfo_account_num = models.CharField(max_length=50, blank=True, null=True)
    bdainfo_ifsc = models.CharField(max_length=20, blank=True, null=True)
    bdainfo_branch = models.CharField(max_length=50, blank=True, null=True)
    bdainfo_holder_name = models.CharField(max_length=50, blank=True, null=True)
    bdainfo_verified_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bdainfo'


class Bdalogins(models.Model):
    bdalogin_id = models.AutoField(primary_key=True)
    bda_fullname = models.CharField(max_length=50)
    bda_email = models.CharField(max_length=50, blank=True, null=True)
    bda_email_verified_at = models.DateTimeField(blank=True, null=True)
    bda_mobile = models.CharField(max_length=15)
    bda_registration_id = models.CharField(max_length=25, blank=True, null=True)
    bda_user_image = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    bda_verification = models.IntegerField(blank=True, null=True)
    verified_date = models.CharField(max_length=20, blank=True, null=True)
    notverified_date = models.CharField(max_length=20, blank=True, null=True)
    bda_user_status = models.IntegerField()
    bda_mgr_status = models.IntegerField(blank=True, null=True)
    admin_bda_mgr_id = models.IntegerField(blank=True, null=True)
    bda_mgr_id = models.IntegerField(blank=True, null=True)
    active_date = models.CharField(max_length=20, blank=True, null=True)
    inctive_date = models.CharField(db_column='Inctive_date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bdalogins'


class Block(models.Model):
    block_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    block_name = models.CharField(max_length=500)
    block_hindi_name = models.CharField(max_length=500)
    dist_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block'


class CallStatus(models.Model):
    calla_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    servey_id = models.IntegerField(blank=True, null=True)
    call_status = models.IntegerField(blank=True, null=True)
    bdalogin_id = models.IntegerField(blank=True, null=True)
    intrest = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'call_status'


class Cast(models.Model):
    cast_id = models.AutoField(primary_key=True)
    cascategoryt_id = models.IntegerField()
    cast_name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cast'


class Castcategory(models.Model):
    castcategory_id = models.AutoField(primary_key=True)
    cascategoryt_name = models.CharField(max_length=120)
    religions_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'castcategory'


class Chapter(models.Model):
    c_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('Subject', models.DO_NOTHING)
    c_name_h = models.TextField()
    c_name_e = models.TextField()
    image = models.TextField()
    status = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chapter'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=500)
    serial_number = models.CharField(max_length=500, blank=True, null=True)
    class_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'class'


class College(models.Model):
    name = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'college'


class District(models.Model):
    dist_id = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=500)
    dist_hindi_name = models.CharField(max_length=500)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'district'


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


class GenerateBdaCount(models.Model):
    bda_count_id = models.AutoField(primary_key=True)
    bdalogin_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_bda_count'


class GenerateBdaMgrCount(models.Model):
    sur_count_mgr_id = models.AutoField(primary_key=True)
    bdalogin_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_bda_mgr_count'


class GenerateManagersurCount(models.Model):
    mgr_sur_id = models.AutoField(primary_key=True)
    mgr_count = models.CharField(max_length=50, blank=True, null=True)
    survey_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_managersur_count'


class GenerateParentRegId(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    total_parent = models.IntegerField(blank=True, null=True)
    survey_id = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_parent_reg_id'


class GenerateStudentRegId(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    total_student = models.IntegerField(blank=True, null=True)
    survey_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_student_reg_id'


class GenerateSurveyCount(models.Model):
    sur_count_id = models.AutoField(primary_key=True)
    survey_id = models.IntegerField(blank=True, null=True)
    sur_count = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'generate_survey_count'


class Hrheadtask(models.Model):
    task_id = models.AutoField(primary_key=True)
    hr_id = models.IntegerField()
    task_name = models.CharField(max_length=200)
    task_start_date = models.TextField()
    task_end_date = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    task_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'hrheadtask'


class Hrinfo(models.Model):
    name = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=12)
    img = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    datebirth = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=7, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    prime_emer_name = models.CharField(max_length=50, blank=True, null=True)
    prime_emer_relationship = models.CharField(max_length=50, blank=True, null=True)
    prime_emer_mobile = models.CharField(max_length=12, blank=True, null=True)
    secon_emer_name = models.CharField(max_length=50, blank=True, null=True)
    secon_emer_relation = models.CharField(max_length=50, blank=True, null=True)
    secon_emer_mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_accound_no = models.CharField(max_length=25, blank=True, null=True)
    back_ifsc = models.CharField(max_length=25, blank=True, null=True)
    bank_branch = models.CharField(max_length=25, blank=True, null=True)
    bank_pan_no = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hrinfo'


class Hrlogins(models.Model):
    regid = models.TextField(blank=True, null=True)
    password = models.TextField()
    status = models.IntegerField()
    role = models.IntegerField()
    monthdata = models.TextField(blank=True, null=True)
    hrhead_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hrlogins'


class InvoiceNo(models.Model):
    survey_id = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_no'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    state_id = models.IntegerField()
    dist_id = models.IntegerField()
    block_id = models.BigIntegerField(blank=True, null=True)
    village_id = models.IntegerField()
    bda_village_complated = models.IntegerField(blank=True, null=True)
    sur_village_complated = models.IntegerField(blank=True, null=True)
    sur_completed_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'location'


class ParentAppInstallInfo(models.Model):
    parent_id = models.IntegerField()
    sur_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parent_app_install_info'


class Parentcallcomment(models.Model):
    call_id = models.AutoField(primary_key=True)
    call_comment = models.TextField()
    call_parent_id = models.IntegerField()
    servey_id = models.IntegerField(blank=True, null=True)
    send_status = models.IntegerField(blank=True, null=True)
    bda_id = models.IntegerField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parentcallcomment'


class Parentinfo(models.Model):
    parent_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    sur_role_status = models.IntegerField()
    parent_user_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    parent_father_name = models.CharField(max_length=500, blank=True, null=True)
    paren_mother_name = models.CharField(max_length=500, blank=True, null=True)
    paren_job = models.CharField(max_length=500, blank=True, null=True)
    parent_registration_id = models.CharField(max_length=500, blank=True, null=True)
    paren_job_discription = models.CharField(max_length=500, blank=True, null=True)
    parent_problem = models.CharField(max_length=500, blank=True, null=True)
    paren_father_mobile = models.CharField(max_length=50, blank=True, null=True)
    paren_father_whatsp_mobile = models.CharField(max_length=15, blank=True, null=True)
    parent_address = models.CharField(max_length=500, blank=True, null=True)
    paren_mother_mobile = models.CharField(max_length=20, blank=True, null=True)
    paren_mother_whatsp_mobile = models.CharField(max_length=20, blank=True, null=True)
    paren_total_chilld = models.CharField(max_length=50, blank=True, null=True)
    smart_phone = models.IntegerField()
    religions_id = models.IntegerField(blank=True, null=True)
    whatsapp_message_status = models.CharField(max_length=500, blank=True, null=True)
    calling_status = models.CharField(max_length=500, blank=True, null=True)
    homestatus = models.CharField(max_length=255, blank=True, null=True)
    call_client_comment = models.TextField(blank=True, null=True)
    castcategory_id = models.IntegerField(blank=True, null=True)
    cast_id = models.IntegerField(blank=True, null=True)
    call_status = models.IntegerField(blank=True, null=True)
    call_status_date = models.DateTimeField(blank=True, null=True)
    crtd_call = models.IntegerField(blank=True, null=True)
    whatsapp_status = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField()
    interest_date = models.CharField(max_length=25, blank=True, null=True)
    sverify_id = models.CharField(max_length=10, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    payment_pay_to = models.IntegerField(blank=True, null=True)
    pay_amount = models.CharField(max_length=50, blank=True, null=True)
    recipet_pname = models.CharField(max_length=50, blank=True, null=True)
    transection_id = models.CharField(max_length=50, blank=True, null=True)
    pament_date = models.DateTimeField(blank=True, null=True)
    subc_for = models.CharField(max_length=500, blank=True, null=True)
    payment_wait = models.IntegerField(blank=True, null=True)
    subscribtion = models.IntegerField(blank=True, null=True)
    pay_image = models.CharField(max_length=500, blank=True, null=True)
    servey_pay_date = models.DateTimeField(blank=True, null=True)
    sub_startdate = models.DateTimeField(blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    verified_date = models.CharField(max_length=50, blank=True, null=True)
    verified_longitude = models.CharField(max_length=50, blank=True, null=True)
    verified_latitude = models.CharField(max_length=50, blank=True, null=True)
    i_sub_services = models.IntegerField(blank=True, null=True)
    visited_status = models.IntegerField(blank=True, null=True)
    pending_date = models.DateTimeField(blank=True, null=True)
    payment_waiting_date = models.DateTimeField(blank=True, null=True)
    reject_date = models.DateTimeField(blank=True, null=True)
    visited_sur_mg_id = models.CharField(max_length=20, blank=True, null=True)
    verified_status = models.IntegerField(blank=True, null=True)
    deliverd_status = models.IntegerField()
    tranf_emp_id = models.IntegerField(blank=True, null=True)
    tranf_emp_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parentinfo'


class Parentlogins(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    parent_info_id = models.IntegerField()
    registration_id = models.CharField(max_length=500, blank=True, null=True)
    user_image = models.CharField(max_length=500, blank=True, null=True)
    user_status = models.CharField(max_length=5)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    login_status = models.IntegerField()
    pin = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parentlogins'


class ParentsFeedback(models.Model):
    parent_id = models.IntegerField()
    survey = models.ForeignKey('Surveyinfo', models.DO_NOTHING)
    feedback = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parents_feedback'


class Question(models.Model):
    ques_id = models.AutoField(primary_key=True)
    test_id = models.IntegerField()
    tittle_h = models.TextField()
    tittle_e = models.TextField()
    ques_image = models.TextField(blank=True, null=True)
    ques_type = models.IntegerField()
    option_e_1 = models.CharField(max_length=50, blank=True, null=True)
    option_e_2 = models.CharField(max_length=50, blank=True, null=True)
    option_e_3 = models.CharField(max_length=50, blank=True, null=True)
    option_e_4 = models.CharField(max_length=50, blank=True, null=True)
    option_h_1 = models.CharField(max_length=50, blank=True, null=True)
    option_h_2 = models.CharField(max_length=50, blank=True, null=True)
    option_h_3 = models.CharField(max_length=50, blank=True, null=True)
    option_h_4 = models.CharField(max_length=50, blank=True, null=True)
    op1_img = models.TextField(blank=True, null=True)
    op2_img = models.TextField(blank=True, null=True)
    op3_img = models.TextField(blank=True, null=True)
    op4_img = models.TextField(blank=True, null=True)
    answer = models.CharField(max_length=50)
    answer_img = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question'


class Religions(models.Model):
    religions_id = models.AutoField(primary_key=True)
    religions_name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'religions'


class SemesterImg(models.Model):
    survey = models.ForeignKey('Surveyinfo', models.DO_NOTHING)
    img_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semester_img'


class SryPayToCompany(models.Model):
    srypay_id = models.AutoField(primary_key=True)
    servey_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    pay_transation_id = models.CharField(max_length=500, blank=True, null=True)
    pay_image = models.TextField(blank=True, null=True)
    sry_amount = models.CharField(max_length=50, blank=True, null=True)
    payment_pay_to = models.IntegerField(blank=True, null=True)
    sry_payment_type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sry_pay_to_company'


class State(models.Model):
    state_name = models.CharField(max_length=500)
    hindi_state_name = models.CharField(max_length=250)
    state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class StudentAttempTest(models.Model):
    sat_id = models.AutoField(primary_key=True)
    std_id = models.CharField(max_length=10)
    question_status = models.TextField()
    attempted_ans = models.TextField()
    test = models.ForeignKey('TestInfo', models.DO_NOTHING)
    correct_ques = models.CharField(max_length=10)
    incorrect_ques = models.CharField(max_length=10)
    skipped_ques = models.CharField(max_length=10)
    marks = models.CharField(max_length=5)
    time = models.TimeField()
    submit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_attemp_test'


class StudentInstallSurInfo(models.Model):
    student_id = models.IntegerField()
    sur_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student_install_sur_info'


class Studentinfo(models.Model):
    student_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    student_regis_number = models.CharField(max_length=500, blank=True, null=True)
    student_fullname = models.CharField(max_length=500)
    student_dob = models.CharField(max_length=25, blank=True, null=True)
    user_image = models.TextField(blank=True, null=True)
    gender = models.IntegerField()
    student_aim = models.TextField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    student_education_status = models.CharField(max_length=500)
    course_id = models.IntegerField(blank=True, null=True)
    exam_id = models.IntegerField(blank=True, null=True)
    be_id = models.IntegerField(blank=True, null=True)
    sem_id = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(db_column='College_name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    student_school_status = models.CharField(max_length=500, blank=True, null=True)
    student_school_board_status = models.CharField(max_length=500, blank=True, null=True)
    school_teachername = models.CharField(max_length=100, blank=True, null=True)
    school_teachercontactno = models.CharField(max_length=11, blank=True, null=True)
    tution_centername = models.CharField(max_length=100, blank=True, null=True)
    tution_teachername = models.CharField(max_length=100, blank=True, null=True)
    tution_teachercontactno = models.CharField(max_length=11, blank=True, null=True)
    married_status = models.IntegerField(blank=True, null=True)
    job_title = models.TextField(blank=True, null=True)
    whats_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    facebook_url = models.CharField(max_length=500, blank=True, null=True)
    linkedin_url = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    agree_parecen = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    status_date = models.DateTimeField(blank=True, null=True)
    active_date = models.DateTimeField(blank=True, null=True)
    inactive_date = models.DateTimeField(blank=True, null=True)
    subscribtion = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    pay_fail_reason = models.CharField(max_length=500, blank=True, null=True)
    sverify_id = models.CharField(max_length=10, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    payment_pay_to = models.IntegerField(blank=True, null=True)
    pay_amount = models.CharField(max_length=50, blank=True, null=True)
    recipet_pname = models.CharField(max_length=50, blank=True, null=True)
    transection_id = models.CharField(max_length=50, blank=True, null=True)
    pament_date = models.DateTimeField(blank=True, null=True)
    expiredate = models.DateTimeField(blank=True, null=True)
    pay_image = models.TextField(blank=True, null=True)
    servey_pay_date = models.DateTimeField(blank=True, null=True)
    sub_i = models.IntegerField(blank=True, null=True)
    sub_startdate = models.DateTimeField(blank=True, null=True)
    year = models.IntegerField()
    deliverd_status = models.IntegerField()
    student_location = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'studentinfo'


class Studentlogins(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    student_info_id = models.IntegerField()
    registration_id = models.CharField(max_length=500, blank=True, null=True)
    user_image = models.CharField(max_length=500, blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pin = models.CharField(max_length=100)
    otp = models.IntegerField()
    loged_device_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'studentlogins'


class StudyNotes(models.Model):
    c = models.ForeignKey(Chapter, models.DO_NOTHING)
    notes_e = models.TextField(blank=True, null=True)
    notes_h = models.TextField(blank=True, null=True)
    img_e = models.TextField(blank=True, null=True)
    img_h = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_notes'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name_h = models.CharField(db_column='subject_name_H', max_length=50)  # Field name made lowercase.
    subject_name_e = models.CharField(db_column='subject_name_E', max_length=50)  # Field name made lowercase.
    s_class_id = models.IntegerField()
    board_id = models.IntegerField()
    s_image = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subject'


class SurveyHistory(models.Model):
    his_id = models.AutoField(primary_key=True)
    survey_id = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.CharField(db_column='Start_Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='End_Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    s_time = models.CharField(max_length=10, blank=True, null=True)
    e_time = models.CharField(max_length=10, blank=True, null=True)
    today_survey = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_history'


class SurveyLogin(models.Model):
    survey_id = models.AutoField(primary_key=True)
    survey_registration_id = models.CharField(max_length=500)
    survey_mobile = models.CharField(max_length=15)
    survey_email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    team_id = models.IntegerField(blank=True, null=True)
    hr_id = models.IntegerField(blank=True, null=True)
    survey_status = models.IntegerField()
    work_status = models.IntegerField()
    verified_status = models.IntegerField(blank=True, null=True)
    traning_start_date = models.DateTimeField(blank=True, null=True)
    training_end_date = models.CharField(max_length=25, blank=True, null=True)
    training_hr_id = models.IntegerField(blank=True, null=True)
    current_team_id = models.IntegerField(blank=True, null=True)
    current_hr_id = models.IntegerField(blank=True, null=True)
    bdt_start_date = models.CharField(max_length=50, blank=True, null=True)
    bdt_end_date = models.CharField(max_length=50, blank=True, null=True)
    bdt_hr_id = models.IntegerField(blank=True, null=True)
    bdt_team_id = models.IntegerField(blank=True, null=True)
    bda_start_date = models.CharField(max_length=50, blank=True, null=True)
    bda_end_date = models.CharField(max_length=50, blank=True, null=True)
    bda_team_id = models.IntegerField(blank=True, null=True)
    bda_hr_id = models.IntegerField(blank=True, null=True)
    verified_date = models.CharField(max_length=20, blank=True, null=True)
    notverify_date = models.CharField(max_length=20, blank=True, null=True)
    survey_code_pin = models.CharField(max_length=4)
    target = models.TextField(blank=True, null=True)
    role = models.IntegerField()
    hided_month = models.TextField()
    otp_ps_login = models.TextField()
    otp_ps_login_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    otp_recovery = models.CharField(max_length=4, blank=True, null=True)
    otp_recovery_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_login'


class Surveyinfo(models.Model):
    survey_info_id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(SurveyLogin, models.DO_NOTHING)
    survey_name = models.CharField(max_length=200, blank=True, null=True)
    assign_state = models.IntegerField(blank=True, null=True)
    assign_dist = models.IntegerField(blank=True, null=True)
    assign_block = models.IntegerField(blank=True, null=True)
    assign_village = models.IntegerField(blank=True, null=True)
    survey_address = models.CharField(max_length=500, blank=True, null=True)
    survey_adhar_number = models.CharField(max_length=15, blank=True, null=True)
    survey_10th_mark = models.CharField(max_length=6, blank=True, null=True)
    survey_12th_mark = models.CharField(max_length=6, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    survey_motor_number = models.CharField(max_length=12, blank=True, null=True)
    survey_adhar_back_image = models.TextField(blank=True, null=True)
    survey_adhar_front_image = models.TextField(blank=True, null=True)
    survey_profile_image = models.TextField(blank=True, null=True)
    driving_licence_img = models.CharField(max_length=200, blank=True, null=True)
    full_size_img = models.CharField(max_length=200, blank=True, null=True)
    college_id_img = models.CharField(max_length=200, blank=True, null=True)
    tenth_img = models.CharField(max_length=200, blank=True, null=True)
    twelth_img = models.CharField(max_length=200, blank=True, null=True)
    address_img = models.CharField(max_length=200, blank=True, null=True)
    vaccination_img = models.CharField(max_length=200, blank=True, null=True)
    police_verification_img = models.CharField(max_length=200, blank=True, null=True)
    profile_img_status = models.IntegerField(blank=True, null=True)
    aadhar_front_uri_status = models.IntegerField(blank=True, null=True)
    aadhar_back_uri_status = models.IntegerField(blank=True, null=True)
    driving_licence_status = models.IntegerField(blank=True, null=True)
    full_size_img_status = models.IntegerField(blank=True, null=True)
    college_id_img_status = models.IntegerField(blank=True, null=True)
    tenth_img_status = models.IntegerField(blank=True, null=True)
    twelth_img_status = models.IntegerField(blank=True, null=True)
    address_img_status = models.IntegerField(blank=True, null=True)
    vaccination_img_status = models.IntegerField(blank=True, null=True)
    police_verification_img_status = models.IntegerField(blank=True, null=True)
    semester_img_status = models.IntegerField(blank=True, null=True)
    highqualification = models.CharField(max_length=20, blank=True, null=True)
    survey_bankname = models.CharField(max_length=50, blank=True, null=True)
    survey_account_num = models.CharField(max_length=100, blank=True, null=True)
    survey_ifsc = models.CharField(db_column='survey_IFSC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    survey_branch = models.CharField(max_length=50, blank=True, null=True)
    passbook_image = models.TextField(blank=True, null=True)
    survey_holder_name = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    current_lattitude = models.CharField(max_length=50, blank=True, null=True)
    current_longitude = models.CharField(max_length=50, blank=True, null=True)
    lastlocation_date = models.DateTimeField(blank=True, null=True)
    order_id = models.TextField()
    voucher = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'surveyinfo'


class SurveyorTarget(models.Model):
    sid = models.IntegerField()
    target = models.CharField(max_length=10)
    month = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'surveyor_target'


class Syllabus(models.Model):
    s_id = models.AutoField(primary_key=True)
    sub_id = models.IntegerField()
    tittle_h = models.CharField(max_length=50)
    tittle_e = models.CharField(max_length=50)
    disc_h = models.TextField()
    disc_e = models.TextField()
    s_image = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syllabus'


class Team(models.Model):
    name = models.CharField(max_length=255)
    hrid = models.IntegerField()
    target = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team'


class TestInfo(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name_e = models.CharField(max_length=50)
    test_name_h = models.CharField(max_length=50)
    test_status = models.IntegerField()
    max_marks = models.CharField(max_length=10)
    total_time = models.CharField(max_length=10, blank=True, null=True)
    sub_id = models.IntegerField(db_column='Sub_id', blank=True, null=True)  # Field name made lowercase.
    c = models.ForeignKey(Chapter, models.DO_NOTHING, blank=True, null=True)
    total_question = models.CharField(max_length=10)
    per_ques_marks = models.IntegerField()
    test_type = models.IntegerField()
    test_level = models.IntegerField()
    state_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    block_id = models.IntegerField(blank=True, null=True)
    village_id = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField()
    board_id = models.IntegerField()
    attempt_time = models.TextField(blank=True, null=True)
    test_description_h = models.TextField(blank=True, null=True)
    test_description_e = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_info'


class TransactionDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey_id = models.ForeignKey(Surveyinfo, models.DO_NOTHING)
    txnid = models.TextField()
    amount = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transaction_details'


class Village(models.Model):
    village_name = models.CharField(max_length=500, db_collation='utf8mb4_unicode_ci')
    village_name_hindi = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    block_id = models.IntegerField()
    dist_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    village_id = models.IntegerField(blank=True, null=True)
    admin_completed_status = models.IntegerField()
    mgr_completed_status = models.IntegerField()
    mgr_completed_date = models.DateTimeField(blank=True, null=True)
    mgr_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'


class Voucher(models.Model):
    code = models.TextField()
    price = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher'
