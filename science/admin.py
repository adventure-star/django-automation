from django.contrib import admin

from .models import TradingPartner, InboundChannel, OutboundChannel, Task, Log

class TradingPartnerAdmin(admin.ModelAdmin):
    fields=['id', 'sftp_hostname', 'sftp_username', 'sftp_password', 'notes']
class InboundChannelAdmin(admin.ModelAdmin):
    fields=['id', 'trading_partner_id', 'folder', 'filename_pattern', 'remove_files']
class OutboundChannelAdmin(admin.ModelAdmin):
    fields=['id', 'trading_partner_id', 'folder', 'archive_folder', 'filename_pattern']
class TaskAdmin(admin.ModelAdmin):
    fields=['id', 'inbound_channel_id', 'outbound_channel_id', 'notification_script']
class LogAdmin(admin.ModelAdmin):
    fields=['task_id', 'inbound_channel_id', 'inbound_trading_partner_id', 'outbound_channel_id', 'outbound_trading_partner_id', 'time', 'inbound_filename', 'inbound_folder', 'outbound_filename', 'outbound_folder', 'log_message']

admin.site.register(TradingPartner, TradingPartnerAdmin)
admin.site.register(InboundChannel, InboundChannelAdmin)
admin.site.register(OutboundChannel, OutboundChannelAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Log, LogAdmin)
