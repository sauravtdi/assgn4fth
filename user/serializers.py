from rest_framework import serializers
from .models import *


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

    def get_start_time(self, obj):
        return obj.start_time.strftime("%B %d %Y %I:%M%p")

    def get_end_time(self, obj):
        return obj.end_time.strftime("%B %d %Y %I:%M%p")


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)
    real_name = serializers.CharField(source='full_name')
    tz = serializers.CharField(source='timezone')

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
