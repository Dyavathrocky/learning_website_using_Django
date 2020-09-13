from django.contrib import admin
from .models import Course , Module , Subject

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug']
    prepopulated_fields = {'slug' : ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['owner' , 'subject', 'title','overview','created']
    list_filter = ['owner' , 'created', 'subject']
    search_fields = ['title' , 'overview']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]
