from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import HomePage, HomePageCourse, HomePageMenthor


class CourseInline(admin.TabularInline):
    model = HomePageCourse
    extra = 1


class MenthorInline(admin.TabularInline):
    model = HomePageMenthor
    extra = 1


class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Greeting Section'), {'fields': ['greeting_background', 'greeting_message', 'greeting_button']}),
        (_('Promoted Courses Section'),
         {'fields': ['promoted_courses_lead', 'promoted_courses_message', 'promoted_courses_button']}),
        (_('Promoted Menthors Section'),
         {'fields': ['promoted_menthors_lead', 'promoted_menthors_message', 'promoted_menthors_button']}),
        (_('Promoted Portfolios Section'),
         {'fields': ['promoted_portfolios_lead', 'promoted_portfolios_message', 'promoted_portfolios_button']}),
        (_('Brand Section'), {'fields': ['brand_logo', 'brand_lead', 'brand_message', 'brand_button']}),
    ]
    inlines = [CourseInline, MenthorInline]


# Register your models here.
admin.site.register(HomePage, HomePageAdmin)
