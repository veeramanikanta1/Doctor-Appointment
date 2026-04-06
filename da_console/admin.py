from django.contrib import admin
from .models import Doctor_App,category,sub_category
from .import models

class doc_admin(admin.ModelAdmin):

    list_display = ('id','full_name','gender','mobile_number','department')
    list_filter = ('full_name',)
    search_fields = ('full_name','mobile_number','department')
    list_display_links = ('id','full_name',)
    # list_editable = ('is_active',)
    # ordering = ('full_name',)
    exclude = ('consultation_languages',)

admin.site.register(Doctor_App,doc_admin)
admin.site.register(category)
admin.site.register(sub_category)


