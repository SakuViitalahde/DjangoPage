from django.contrib import admin
from .models import Project
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


#Jos halutaan otsikoida ja ryhmitellä kentti se voidaan tehdä näin
#Jos kenttiä ei haluta näyttä kaikki voidaan niiden esitysmuotoa säätää asettamalla fieldsiin taulukko kentistä jota esitetään
##class ProjectAdmin(admin.ModelAdmin):
##    fieldsets = [
##        ("Title/Date", {'fields': ["project_title, project_published"]}),
##        ("Content", {'fields': ["project_content"]})
##    ]


class ProjAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["project_title", "project_published"]}),
        ("Content", {"fields": ["project_content", "project_description"]})
    ]

    # Lisätään textfieldeihin tinymce widgetti joka tekee texti editorista kivemman näköisen
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Project,ProjAdmin)

# jos ei haluta erillisiä asetuskia adminille
##admin.site.register(Project)