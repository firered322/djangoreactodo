from rest_framework import serializers
from .models import Bucket, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'bucket', 'job_todo', 'completed')
