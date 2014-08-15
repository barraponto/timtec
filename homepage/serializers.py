from .models import HomePage
from rest_framework import serializers


class HomePageSerializer(serializers.ModelSerializer):

      image_section_initial = serializers.Field(source='get_image_section_initial_url')
      image_section_enois = serializers.Field(source='get_image_section_enois_url')

      class Meta:
          model = HomePage
