from django.db import models

class ArSystems(models.Model):
    system_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=300)
    active = models.BooleanField(default=True)  # Mapeo de bit(1)
    creation_date = models.DateField()  # Solo fecha
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_systems'


class ArRoles(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=200)
    control = models.CharField(max_length=1)
    creation_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_roles'


class ArSystemOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    system = models.ForeignKey(ArSystems, on_delete=models.CASCADE, db_column='system_id')  # ON DELETE CASCADE
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    activation_date = models.DateField()
    disable_date = models.DateField(null=True, blank=True)
    menu = models.BooleanField(null=True, blank=True)
    sequence = models.BigIntegerField(null=True, blank=True)
    parent_option = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent_option_id')
    icon_svg = models.CharField(max_length=2000, null=True, blank=True)
    creation_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_system_options'


class ArRoleOptions(models.Model):
    role_option_id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey(ArRoles, on_delete=models.DO_NOTHING, db_column='role_id')  # ON DELETE NO ACTION
    option = models.ForeignKey(ArSystemOptions, on_delete=models.DO_NOTHING, db_column='option_id')
    active = models.BooleanField(default=True)
    activation_date = models.DateField()
    disable_date = models.DateField(null=True, blank=True)
    creation_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_role_options'


class ArStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    short_name = models.CharField(max_length=3)
    created_by = models.BigIntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(null=True, blank=True)
    modified_by = models.BigIntegerField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ar_status'


class ArUsers(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=300)
    additional_emails = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=80)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    expiration_date = models.DateField()
    blocked = models.BooleanField(default=False)
    country_code = models.CharField(max_length=4)
    state_code = models.CharField(max_length=4, null=True, blank=True)
    city_code = models.CharField(max_length=4, null=True, blank=True)
    recovery_timeout = models.DateTimeField(null=True, blank=True)
    failed_auth = models.IntegerField(default=0)
    super_user = models.BooleanField(default=False)
    creation_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_users'


class ArBooks(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=200)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    z = models.IntegerField(null=True, blank=True)
    standard_time = models.BigIntegerField(null=True, blank=True)
    timeout = models.BigIntegerField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.BigIntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(null=True, blank=True)
    modified_by = models.BigIntegerField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ar_books'


class ArDeliveries(models.Model):
    delivery_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ArUsers, on_delete=models.DO_NOTHING, db_column='user_id')
    book = models.ForeignKey(ArBooks, on_delete=models.DO_NOTHING, db_column='book_isbn')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(ArStatus, on_delete=models.DO_NOTHING, db_column='status_id')
    notes = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.BigIntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(null=True, blank=True)
    modified_by = models.BigIntegerField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ar_deliveries'


class ArUserRoles(models.Model):
    user_role_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ArUsers, on_delete=models.DO_NOTHING, db_column='user_id')
    role = models.ForeignKey(ArRoles, on_delete=models.DO_NOTHING, db_column='role_id')
    activation_date = models.DateField()
    disable_date = models.DateField(null=True, blank=True)
    creation_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ar_user_roles'


