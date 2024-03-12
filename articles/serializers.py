from rest_framework import serializers
from .models import Articlesdata

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlesdata
        fields = ['id', 'title', 'content', 'author']