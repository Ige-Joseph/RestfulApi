from rest_framework import serializers
from .models import Books


class Books_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author', 'published_date']
        # fields = '__all__'