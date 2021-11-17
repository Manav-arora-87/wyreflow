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
    survey_registration_id = models.CharField(max_length=500, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'survey_login'


class Surveyinfo(models.Model):
    survey_info_id = models.AutoField(primary_key=True)
    survey_id = models.IntegerField(blank=True, null=True)
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
