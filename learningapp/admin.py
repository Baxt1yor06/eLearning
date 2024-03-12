from django.contrib import admin
from .models import Index_carousel,Skils,About,Courses,Popular_courses,Instructors,Clients,Contact
# Register your models here.

@admin.register(Index_carousel)
class Index_carouselAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name1','bio']
    prepopulated_fields = {"slug": ('name1',)}

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Popular_courses)
class Popular_coursesAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Instructors)
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Skils)
admin.site.register(Contact)
