# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Good_or_Bad, Result


class GoodOrBadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good_or_Bad
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

