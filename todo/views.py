from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Bucket, Todo

# Creating a bucket:
#   from todo.models import Bucket, Todo
#   b1 = Bucket(bucket_name="customBucket")
#   b1.save()
# Creating a todo inside the bucket:
#   b1.todos.create(job_todo="do the job")


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Bucket.objects.all()
