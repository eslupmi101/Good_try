from django.contrib import admin

from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'description',
        'pub_date',
        'customer',
    )
    search_fields = ('description',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Data, DataAdmin)
