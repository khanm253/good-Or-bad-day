# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Good_or_Bad


class GoodOrBadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good_or_Bad
        fields = '__all__'