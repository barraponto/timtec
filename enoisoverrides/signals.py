from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Course
from course_material.models import CourseMaterial

@receiver(post_save, sender=Course)
def create_course_material_on_course_creation(sender, **kwargs):
    if kwargs.get('created', False):
        CourseMaterial.objects.get_or_create(course=kwargs.get('instance'))
