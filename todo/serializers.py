from rest_framework import serializers
from .models import Bucket, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('bucket_name', 'job_todo', 'completed')
