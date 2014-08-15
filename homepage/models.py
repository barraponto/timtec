import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode
from core.models import Course
from accounts.models import TimtecUser


def unidecode_path(prefix):
    def wrapper(instance, filename):
        filename = unidecode(filename)
        # return the whole path to the file
        return os.path.join(prefix, filename)
    return wrapper


class HomePage(models.Model):
    greeting_background = models.ImageField(
        _('Greeting Background'),
        upload_to=unidecode_path('home_page_pictures'),
        blank=True)
    greeting_message = models.TextField(_('Greeting Message'), blank=True)
    greeting_button = models.CharField(
        _('Greeting Button'), max_length=64, blank=True)

    promoted_courses_lead = models.CharField(
        _('Promoted Courses Lead'), max_length=128, blank=True)
    promoted_courses_message = models.TextField(
        _('Promoted Courses Message'), blank=True)
    promoted_courses_button = models.CharField(
        _('Promoted Courses Button'), max_length=64, blank=True)

    promoted_menthors_lead = models.CharField(
        _('Promoted Menthors Lead'), max_length=128, blank=True)
    promoted_menthors_message = models.TextField(_('Promoted Menthors Message'), blank=True)
    promoted_menthors_button = models.CharField(
        _('Promoted Menthors Button'), max_length=64, blank=True)

    promoted_portfolios_lead = models.CharField(
        _('Promoted Portfolios Lead'), max_length=128, blank=True)
    promoted_portfolios_message = models.TextField(_('Promoted Portfolios Message'), blank=True)
    promoted_portfolios_button = models.CharField(
        _('Promoted Portfolios Button'), max_length=64, blank=True)

    brand_logo = models.ImageField(
        _('Brand Section Logo'),
        upload_to=unidecode_path('home_page_pictures'),
        blank=True)
    brand_lead = models.CharField(
        _('Brand Lead'), max_length=128, blank=True)
    brand_message = models.TextField(_('Brand Message'), blank=True)
    brand_button = models.CharField(
        _('Brand Button'), max_length=64, blank=True)

    promoted_courses = models.ManyToManyField(Course, related_name='+',
                                              through='HomePageCourse',
                                              blank=True)

    promoted_menthors = models.ManyToManyField(
        TimtecUser, related_name='+', through='HomePageMenthor', blank=True)

    def get_image_section_initial_url(self):
        return self.image_section_initial.url

    def get_image_section_enois_url(self):
        return self.image_section_enois.url

    class Meta:
        verbose_name = _('HomePage')
        verbose_name_plural = _('HomePages')


class HomePageCourse(models.Model):
    homepage = models.ForeignKey(HomePage)
    course = models.ForeignKey(Course)

    class Meta:
        unique_together = (('homepage', 'course'),)


class HomePageMenthor(models.Model):
    homepage = models.ForeignKey(HomePage)
    menthor = models.ForeignKey(TimtecUser)

    class Meta:
        unique_together = (('homepage', 'menthor'),)
