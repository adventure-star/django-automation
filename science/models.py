from django.db import models

from django.core.validators import RegexValidator
id_validator = RegexValidator(r"^[-a-z0-9_]+$", "Please insert efficient id!")
archive_validator = RegexValidator(r"^[-a-z0-9_/]*$", "Please insert efficient value!")

class TradingPartner(models.Model):
    id=models.CharField(
        blank=False,
        primary_key=True,
        max_length=50,
        validators=[id_validator],
        verbose_name=u"Trading Partner ID"
    )
    sftp_hostname=models.CharField(blank=True, max_length=100, verbose_name=u"SFTP Hostname")
    sftp_username=models.CharField(blank=True, max_length=50, verbose_name=u"SFTP Username")
    sftp_password=models.CharField(blank=True, max_length=50, verbose_name=u"SFTP Password")
    notes=models.CharField(blank=True, max_length=200, verbose_name=u"Notes")

    def __str__(self):
        return self.id

class InboundChannel(models.Model):
    id=models.CharField(
        blank=False,
        max_length=50,
        primary_key=True,
        validators=[id_validator],
        verbose_name=u"Inbound Channel ID"
    )
    trading_partner_id=models.ForeignKey(TradingPartner, on_delete=models.PROTECT, null=False, verbose_name=u"Trading Partner ID")
    folder=models.CharField(blank=True, max_length=100, verbose_name=u"Folder")
    filename_pattern=models.CharField(blank=False, max_length=100, verbose_name=u"Filename Pattern")
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    remove_files=models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False, verbose_name=u"Remove Files")

    def __str__(self):
        return self.id

class OutboundChannel(models.Model):
    id=models.CharField(
        blank=False,
        max_length=50,
        primary_key=True,
        validators=[id_validator],
        verbose_name=u"Outbound Channel ID"
    )
    trading_partner_id=models.ForeignKey(TradingPartner, on_delete=models.PROTECT, null=False, verbose_name=u"Trading Partner ID")
    folder=models.CharField(blank=True, max_length=100, verbose_name=u"Folder")
    archive_folder=models.CharField(blank=True, max_length=100, validators=[archive_validator], verbose_name=u"Archive Folder")
    filename_pattern=models.CharField(blank=False, max_length=100, verbose_name=u"Filename Pattern")

    def __str__(self):
        return self.id

class Task(models.Model):
    id=models.CharField(
        blank=False,
        max_length=50,
        primary_key=True,
        validators=[id_validator],
        verbose_name=u"Task ID"
    )
    inbound_channel_id=models.ForeignKey(InboundChannel, on_delete=models.PROTECT, null=False, verbose_name=u"Inbound Channel ID")
    outbound_channel_id=models.ForeignKey(OutboundChannel, on_delete=models.PROTECT, null=False, verbose_name=u"Outbound Channel ID")
    notification_script=models.CharField(blank=True, max_length=200, verbose_name=u"Notification Script")

    def __str__(self):
        return self.id
    
class Log(models.Model):
    task_id=models.CharField(blank=True, max_length=50, verbose_name=u"Task ID")
    inbound_channel_id=models.CharField(blank=True, max_length=50, verbose_name=u"Inbound Channel ID")
    inbound_trading_partner_id=models.CharField(blank=True, max_length=50, verbose_name=u"Inbound Trading Partner ID")
    outbound_channel_id=models.CharField(blank=True, max_length=50, verbose_name=u"Outbound Channel ID")
    outbound_trading_partner_id=models.CharField(blank=True, max_length=50, verbose_name=u"Outbound Trading Partner ID")
    time=models.DateTimeField('time')
    inbound_filename=models.CharField(blank=True, max_length=100, verbose_name=u"Inbound Filename")
    inbound_folder=models.CharField(blank=True, max_length=100, verbose_name=u"Inbound Folder")
    outbound_filename=models.CharField(blank=True, max_length=100, verbose_name=u"Outbound Filename")
    outbound_folder=models.CharField(blank=True, max_length=100, verbose_name=u"Outbound Folder")
    log_message=models.CharField(blank=True, max_length=100, verbose_name=u"Log Message")

