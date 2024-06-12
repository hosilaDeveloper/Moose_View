from django.contrib import admin
from contact.models import Contact, Subscriber

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name', 'email', 'subject')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber)
