from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ParkingLot, FineTip

class FineTipAdmin(admin.ModelAdmin):

    readonly_fields = ["finetip_image"]

    def finetip_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width/2,
            height=obj.image.height/2,
            )
    )

# Register your models here.
admin.site.register(ParkingLot)
admin.site.register(FineTip, FineTipAdmin)
#admin.site.register(FineTip)

admin.AdminSite.site_header = "Finedr"
admin.AdminSite.site_title = "Finedr"
admin.AdminSite.site_url = None
