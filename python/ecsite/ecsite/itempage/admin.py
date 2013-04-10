# -*- coding: utf-8 -*-
from django.contrib import admin
from ecsite.itempage.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name','price') # 一覧表示したいフィールドを設定

#admin.site.register(Item)
admin.site.register(Item,ItemAdmin) #ItemAdminクラスも追加
