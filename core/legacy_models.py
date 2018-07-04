# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Confirmation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    structures_damaged = models.IntegerField(db_column='Structures_Damaged')  # Field name made lowercase.
    people_injured = models.IntegerField(db_column='People_Injured')  # Field name made lowercase.
    people_killed = models.IntegerField(db_column='People_Killed')  # Field name made lowercase.
    fire_dept_reported = models.TextField(db_column='Fire_Dept_Reported')  # Field name made lowercase.
    time_of_call = models.DateTimeField(db_column='Time_Of_Call')  # Field name made lowercase.
    number_called = models.TextField(db_column='Number_Called')  # Field name made lowercase.
    time_of_dispatch = models.DateTimeField(db_column='Time_Of_Dispatch')  # Field name made lowercase.
    time_of_first_vehicle = models.DateTimeField(db_column='Time_Of_First_Vehicle')  # Field name made lowercase.
    cause = models.TextField(db_column='Cause')  # Field name made lowercase.
    time_of_incident = models.DateTimeField(db_column='Time_Of_Incident')  # Field name made lowercase.
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=50)
    question3 = models.DateField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.TextField()
    question8 = models.CharField(max_length=10)
    question9 = models.TextField()
    question10 = models.CharField(max_length=10)
    question11 = models.CharField(max_length=10)
    question12 = models.CharField(max_length=10)
    question13 = models.CharField(max_length=10)
    question14 = models.IntegerField()
    question15 = models.CharField(max_length=50)
    question16 = models.CharField(max_length=10)
    question17 = models.DateTimeField()
    question18 = models.CharField(max_length=10)
    question19 = models.CharField(max_length=10)
    question20 = models.CharField(max_length=10)
    question21 = models.CharField(max_length=250)
    question22 = models.CharField(max_length=250)
    reporter_name = models.CharField(max_length=100)
    reporter_lastname = models.CharField(max_length=100)
    reporter_mobile = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'Confirmation'


class Confirmationheartbeat(models.Model):
    confirmation_id = models.IntegerField()
    heartbeat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ConfirmationHeartbeat'


class EmailAddresses(models.Model):
    index = models.BigAutoField(db_column='INDEX', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40)  # Field name made lowercase.
    email_address = models.CharField(db_column='EMAIL_ADDRESS', max_length=50)  # Field name made lowercase.
    phone_num = models.CharField(db_column='PHONE_NUM', max_length=14)  # Field name made lowercase.
    info_level = models.IntegerField(db_column='INFO_LEVEL')  # Field name made lowercase.
    section_list = models.TextField(db_column='SECTION_LIST')  # Field name made lowercase.
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'Email_Addresses'


class Heartbeats(models.Model):
    beat_num = models.BigAutoField(db_column='Beat_num', primary_key=True)  # Field name made lowercase.
    uid = models.CharField(db_column='uID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    sniffer_num = models.IntegerField(db_column='Sniffer_num', blank=True, null=True)  # Field name made lowercase.
    alert_level = models.IntegerField(db_column='Alert_level', blank=True, null=True)  # Field name made lowercase.
    alert_data = models.IntegerField(db_column='Alert_data')  # Field name made lowercase.
    batt_level = models.IntegerField(db_column='Batt_level', blank=True, null=True)  # Field name made lowercase.
    sig_strength = models.IntegerField(db_column='Sig_Strength', blank=True, null=True)  # Field name made lowercase.
    mesh_rssi = models.IntegerField()
    gps_time = models.TimeField(db_column='GPS_time', blank=True, null=True)  # Field name made lowercase.
    gps_date = models.DateField(db_column='GPS_date', blank=True, null=True)  # Field name made lowercase.
    gps_lock = models.IntegerField(db_column='GPS_lock', blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=30, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=30, blank=True, null=True)  # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp')  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    sim = models.IntegerField(db_column='SIM', blank=True, null=True)  # Field name made lowercase.
    reset = models.IntegerField(db_column='Reset', blank=True, null=True)  # Field name made lowercase.
    server_time = models.BigIntegerField(db_column='Server_Time')  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='Date_Time', blank=True, null=True)  # Field name made lowercase.
    confirmation_id = models.CharField(db_column='Confirmation_ID', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Heartbeats'


class Registration(models.Model):
    index = models.BigAutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    opt_out = models.IntegerField(db_column='Opt_Out')  # Field name made lowercase.
    registered_succesfully = models.IntegerField(db_column='Registered_Succesfully')  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=15)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=10)  # Field name made lowercase.
    interactions = models.IntegerField(db_column='Interactions')  # Field name made lowercase.
    failures = models.IntegerField(db_column='Failures')  # Field name made lowercase.
    initial_date = models.DateTimeField(db_column='Initial_Date', blank=True, null=True)  # Field name made lowercase.
    last_date = models.DateTimeField(db_column='Last_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registration'


class RegistrationLog(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    api_id = models.CharField(db_column='Api_ID', max_length=8)  # Field name made lowercase.
    from_num = models.CharField(db_column='From_Num', max_length=15)  # Field name made lowercase.
    to_num = models.CharField(db_column='To_Num', max_length=15)  # Field name made lowercase.
    mo_id = models.CharField(db_column='Mo_ID', max_length=12)  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registration_Log'


class SentMessages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    area_code = models.CharField(db_column='Area_Code', max_length=6)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.
    date_sent = models.DateTimeField(db_column='Date_Sent')  # Field name made lowercase.
    end_users = models.IntegerField(db_column='End_Users')  # Field name made lowercase.
    device_uid = models.CharField(max_length=12)
    result = models.TextField(db_column='Result')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sent_Messages'


class SnifferErrors(models.Model):
    index = models.BigAutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    sniffer_num = models.IntegerField(db_column='Sniffer_num')  # Field name made lowercase.
    error_code = models.CharField(db_column='Error_code', max_length=20)  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=300)  # Field name made lowercase.
    sig_strength = models.IntegerField(db_column='Sig_Strength')  # Field name made lowercase.
    batt_level = models.IntegerField(db_column='Batt_level')  # Field name made lowercase.
    error_time = models.DateTimeField(db_column='Error_Time')  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='Date_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sniffer_Errors'


class SniffersAreas(models.Model):
    index = models.BigAutoField(db_column='INDEX', primary_key=True)  # Field name made lowercase.
    sniffer_num = models.BigIntegerField(db_column='SNIFFER_NUM')  # Field name made lowercase.
    phone_num = models.TextField(db_column='PHONE_NUM')  # Field name made lowercase.
    area_name = models.CharField(db_column='AREA_NAME', max_length=50)  # Field name made lowercase.
    startnetfunc = models.IntegerField(db_column='StartNetFunc')  # Field name made lowercase.
    stopnetfunc = models.IntegerField(db_column='StopNetFunc')  # Field name made lowercase.
    ringalarms = models.IntegerField(db_column='RingAlarms')  # Field name made lowercase.
    silenttest = models.IntegerField(db_column='SilentTest')  # Field name made lowercase.
    batt_level = models.IntegerField(db_column='BATT_LEVEL')  # Field name made lowercase.
    last_heartbeat = models.DateTimeField(db_column='LAST_HEARTBEAT')  # Field name made lowercase.
    monitoring = models.IntegerField(db_column='MONITORING')  # Field name made lowercase.
    last_checked = models.DateTimeField(db_column='LAST_CHECKED')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6)  # Field name made lowercase.
    county = models.IntegerField()
    sensitivity = models.IntegerField()
    status = models.IntegerField()
    gps_lat = models.CharField(max_length=250)
    gps_long = models.CharField(max_length=250)
    gps_lat_average = models.CharField(max_length=100)
    gps_long_average = models.CharField(max_length=100)
    device_installed = models.IntegerField(blank=True, null=True)
    new = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Sniffers_Areas'


class StatusPings(models.Model):
    sniffer_number = models.IntegerField(db_column='Sniffer_number')  # Field name made lowercase.
    uid = models.CharField(db_column='uID', max_length=11)  # Field name made lowercase.
    status_data = models.IntegerField(db_column='Status_Data')  # Field name made lowercase.
    max_temp = models.SmallIntegerField(db_column='Max_Temp')  # Field name made lowercase.
    min_temp = models.SmallIntegerField(db_column='Min_Temp')  # Field name made lowercase.
    ror10_max = models.SmallIntegerField(db_column='ROR10_Max')  # Field name made lowercase.
    batt_volt = models.CharField(db_column='Batt_Volt', max_length=20)  # Field name made lowercase.
    rssi = models.FloatField(db_column='RSSI')  # Field name made lowercase.
    mesh_rssi = models.SmallIntegerField()
    server_time = models.DateTimeField(db_column='Server_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Status_Pings'


class UniqueIds(models.Model):
    device_id = models.IntegerField(db_column='Device_ID')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    firmware_version = models.CharField(db_column='Firmware_Version', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unique_IDs'


class WeatherData(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    sniffer_num = models.IntegerField(db_column='Sniffer_Num')  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='Date_Time')  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=11)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=11)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=11)  # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp')  # Field name made lowercase.
    humidity = models.IntegerField(db_column='Humidity')  # Field name made lowercase.
    cloud_percentage = models.IntegerField(db_column='Cloud_Percentage')  # Field name made lowercase.
    wind_speed = models.IntegerField(db_column='Wind_Speed')  # Field name made lowercase.
    wind_direction = models.IntegerField(db_column='Wind_Direction')  # Field name made lowercase.
    rain = models.IntegerField(db_column='Rain')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Weather_Data'


class AgentCheckIn(models.Model):
    agent_id = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_check_in'


class AgentClientAction(models.Model):
    agent_id = models.IntegerField()
    device_id = models.IntegerField()
    action_type = models.CharField(max_length=250)
    created = models.DateTimeField()
    meta_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_client_action'


class AgentClientCollection(models.Model):
    agent_user_id = models.IntegerField()
    device_id = models.IntegerField()
    payment_type = models.CharField(max_length=250)
    payment_amount = models.CharField(max_length=250)
    payment_signature_image = models.TextField()
    payment_photo = models.TextField()
    created = models.DateTimeField()
    status = models.CharField(max_length=250)
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'agent_client_collection'


class AgentClientCollectionAllocation(models.Model):
    device_id = models.IntegerField()
    agent_client_collection_id = models.IntegerField()
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_client_collection_allocation'


class AgentClientVisit(models.Model):
    agent_user_id = models.IntegerField()
    device_id = models.IntegerField()
    visit_type = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_client_visit'


class AgentLead(models.Model):
    agent_user_id = models.IntegerField()
    lead_name = models.CharField(max_length=250)
    lead_mobile = models.CharField(max_length=10)
    lead_action = models.CharField(max_length=250)
    lead_follow_up_datetime = models.DateTimeField()
    lead_source = models.TextField()
    status = models.CharField(max_length=250)
    closed_reason = models.TextField()
    lead_created = models.DateTimeField()
    lead_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_lead'


class AgentNotification(models.Model):
    agent_id = models.IntegerField()
    heartbeat_id = models.IntegerField()
    notification_type = models.CharField(max_length=250)
    area_code = models.CharField(max_length=250)
    created = models.DateTimeField()
    notification_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_notification'


class AgentSchedule(models.Model):
    agent_id = models.IntegerField()
    schedule_date = models.DateField()
    schedule_slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_schedule'


class AgentTechnicalVisit(models.Model):
    agent_id = models.IntegerField()
    device_id = models.IntegerField()
    created = models.DateTimeField()
    meta = models.TextField()
    location_latitude = models.CharField(max_length=250)
    location_longitude = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'agent_technical_visit'


class AgentTransaction(models.Model):
    agent_id = models.IntegerField()
    description = models.CharField(max_length=250)
    transaction_value = models.CharField(max_length=100)
    agent_client_collection_id = models.IntegerField()
    created_by = models.CharField(max_length=250)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_transaction'


class AgentUser(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=128)
    salt = models.CharField(max_length=32)
    login_count = models.IntegerField()
    last_login = models.DateTimeField()
    created = models.DateTimeField()
    mobile_number = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'agent_user'


class AgentUserArea(models.Model):
    agent_user_id = models.IntegerField()
    area_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_user_area'


class AgentVisit(models.Model):
    agent_id = models.IntegerField()
    device_id = models.IntegerField()
    created = models.DateTimeField()
    checklist_1 = models.TextField()
    checklist_2 = models.TextField()
    checklist_3 = models.TextField()
    checklist_4 = models.TextField()
    checklist_5 = models.TextField()
    checklist_6 = models.TextField()
    checklist_7 = models.TextField()
    checklist_8 = models.TextField()
    checklist_9 = models.TextField()
    checklist_pop = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'agent_visit'



class BytemoneyApi(models.Model):
    device_id = models.IntegerField()
    api_result = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bytemoney_api'


class ClientPhotoHistory(models.Model):
    device_id = models.BigIntegerField()
    photo_type = models.CharField(max_length=250)
    photo_path = models.CharField(max_length=250)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_photo_history'


class Country(models.Model):
    country_code = models.CharField(max_length=2)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'country'


class Device(models.Model):
    device_barcode = models.CharField(max_length=128)
    location_gps_latitude = models.CharField(max_length=64)
    location_gps_longitude = models.CharField(max_length=64)
    location_name = models.CharField(max_length=250)
    location_house_number = models.CharField(max_length=64)
    location_number_rooms = models.IntegerField()
    location_household_language = models.CharField(max_length=250)
    location_household_value = models.CharField(max_length=250)
    location_front_door_image = models.CharField(max_length=250)
    location_front_door_image_type = models.CharField(max_length=32)
    customer_first_name = models.CharField(max_length=250)
    customer_last_name = models.CharField(max_length=250)
    customer_mobile_number = models.CharField(max_length=64)
    device_photo = models.CharField(max_length=250)
    device_photo_type = models.IntegerField()
    system_created = models.DateTimeField()
    system_agent_id = models.IntegerField()
    system_agent_info = models.CharField(max_length=250)
    system_app_type = models.CharField(max_length=250)
    notes = models.TextField()
    sniffers_areas_code = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=50)
    agent_mobile_number = models.CharField(max_length=30)
    receive_sms = models.IntegerField()
    insurance_policy_number = models.CharField(max_length=250)
    insurance_policy_type_name = models.CharField(max_length=250)
    insurance_policy_premium = models.IntegerField()
    insurance_expected_payment_method = models.CharField(max_length=250)
    insurance_expected_payment_date = models.IntegerField()
    insurance_policy_lapse_date = models.DateField()
    insurance_application_captured_date = models.DateField()
    insurance_policy_sign_up_date = models.DateField()
    insurance_commencement_date = models.DateField()
    insurance_agent_name = models.CharField(max_length=250)
    insurance_region_name = models.CharField(max_length=250)
    insurance_last_verification_date = models.DateField()
    insurance_member_name = models.CharField(max_length=250)
    insurance_member_ids = models.CharField(max_length=250)
    insurance_cellphone_number = models.CharField(max_length=20)
    insurance_alternative_contact_details = models.CharField(max_length=20)
    insurance_physical_addresses = models.CharField(max_length=250)
    insurance_date_of_birth = models.DateField()
    insurance_gender = models.CharField(max_length=20)
    insurance_agent_vendor_id = models.IntegerField()
    insurance_kin_first_name = models.CharField(max_length=250)
    insurance_kin_last_name = models.CharField(max_length=250)
    insurance_kin_id_number = models.CharField(max_length=250)
    insurance_kin_dob = models.CharField(max_length=250)
    insurance_kin_gender = models.CharField(max_length=250)
    insurance_kin_cell = models.CharField(max_length=250)
    insurance_referral_name = models.CharField(max_length=250)
    insurance_income_source = models.CharField(max_length=250)
    photo_outside = models.CharField(max_length=250)
    photo_left = models.CharField(max_length=250)
    photo_right = models.CharField(max_length=250)
    photo_client = models.CharField(max_length=250)
    photo_device = models.CharField(max_length=250)
    photo_inside_left = models.CharField(max_length=250)
    photo_inside_right = models.CharField(max_length=250)
    photo_inside_one = models.CharField(max_length=250)
    photo_inside_two = models.CharField(max_length=250)
    system_contract_received = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'device'


class DeviceHouseholdOccupant(models.Model):
    device_id = models.IntegerField()
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    id_number = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'device_household_occupant'


class DeviceMerge(models.Model):
    device_barcode = models.CharField(max_length=128)
    location_gps_latitude = models.CharField(max_length=64)
    location_gps_longitude = models.CharField(max_length=64)
    location_name = models.CharField(max_length=250)
    location_house_number = models.CharField(max_length=64)
    location_number_rooms = models.IntegerField()
    location_front_door_image = models.CharField(max_length=250)
    location_front_door_image_type = models.CharField(max_length=32)
    customer_first_name = models.CharField(max_length=250)
    customer_last_name = models.CharField(max_length=250)
    customer_mobile_number = models.CharField(max_length=64)
    device_photo = models.CharField(max_length=250)
    device_photo_type = models.IntegerField()
    system_created = models.DateTimeField()
    system_agent_id = models.IntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_merge'


class Feed(models.Model):
    type_id = models.IntegerField()
    message = models.CharField(max_length=250)
    created = models.DateTimeField()
    area_code = models.CharField(max_length=20, blank=True, null=True)
    device_uid = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'feed'


class FeedUser(models.Model):
    user_id = models.IntegerField()
    feed_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feed_user'


class FieldTestLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(db_column='uID', max_length=11)  # Field name made lowercase.
    sniffer_num = models.CharField(db_column='Sniffer_num', max_length=6)  # Field name made lowercase.
    alert_level = models.IntegerField(db_column='Alert_level')  # Field name made lowercase.
    alert_data = models.CharField(db_column='Alert_data', max_length=11)  # Field name made lowercase.
    mesh_rssi = models.IntegerField()
    date_time = models.DateTimeField(db_column='Date_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'field_test_log'


class Impact(models.Model):
    key = models.IntegerField(unique=True)
    kills = models.FloatField()
    injures = models.FloatField()
    destroys = models.FloatField()
    displaces = models.FloatField()
    municipality_cost = models.IntegerField()
    average_shack_value = models.IntegerField()
    total_shacks_sa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'impact'


class PushToPay(models.Model):
    uid = models.CharField(db_column='uID', max_length=10)  # Field name made lowercase.
    gateway_imei = models.IntegerField()
    is_a_client_at_time_of_push = models.IntegerField()
    agent_at_time_of_push = models.IntegerField()
    detector_batt_level = models.IntegerField()
    rssi = models.IntegerField()
    time_created = models.DateTimeField()
    payment_collected_within_hour = models.IntegerField()
    payment_collected_within_day = models.IntegerField()
    alert_level = models.IntegerField()
    sms_was_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'push_to_pay'


class PushToPayFieldTest(models.Model):
    uid = models.CharField(db_column='uID', max_length=10)  # Field name made lowercase.
    gateway_imei = models.IntegerField()
    detector_batt_level = models.IntegerField()
    rssi_threshold = models.IntegerField()
    gateway_rssi = models.IntegerField()
    alert_level = models.IntegerField()
    time_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'push_to_pay_field_test'


class ResponseInfo(models.Model):
    registration_log_id = models.IntegerField()
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    created = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'response_info'


class Settings(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    sms_time_limit = models.IntegerField()
    alerts_status = models.IntegerField()
    battery_level_warning = models.IntegerField()
    heartbeat_time = models.IntegerField()
    ring_fence_distance = models.IntegerField()
    agent_timeout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settings'


class SigfoxHeartbeats(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(db_column='uID', max_length=11)  # Field name made lowercase.
    sniffer_num = models.CharField(db_column='Sniffer_num', max_length=6)  # Field name made lowercase.
    alert_level = models.IntegerField(db_column='Alert_level')  # Field name made lowercase.
    alert_data = models.CharField(db_column='Alert_data', max_length=11)  # Field name made lowercase.
    mesh_rssi = models.IntegerField()
    rssi = models.FloatField()
    snr = models.FloatField()
    snr_avg = models.FloatField()
    date_time = models.DateTimeField(db_column='Date_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sigfox_heartbeats'
