from django.contrib import admin
from .models import Product, Cart,Pay,ContactUs,UserMessage
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Pay)
admin.site.register(UserMessage)


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']