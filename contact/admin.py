from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin (admin.ModelAdmin):#heritage
    list_display = ('listing','customer','subject')
    list_display_links=('customer','subject')
    list_filter = ('listing','customer','subject')
    search_fields=('subject',)
          

admin.site.register(Contact,ContactAdmin)