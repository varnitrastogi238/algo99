from django.contrib import admin

# Register your models here.

from .models import User1,BOT,BOT1,BOT2,BOT3,BOT4,orders,tradingview_orders,dashboard_analysis
admin.site.register(User1)
admin.site.register(BOT)
admin.site.register(BOT1)
admin.site.register(BOT2)
admin.site.register(BOT3)
admin.site.register(BOT4)
admin.site.register(orders)
admin.site.register(tradingview_orders)
admin.site.register(dashboard_analysis)