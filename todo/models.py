from django.db import models


class Bucket(models.Model):
    bucket_name = models.CharField(max_length=100)

    def __str__(self):
        return self.bucket_name


class Todo(models.Model):
    job_todo = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    bucket = models.ForeignKey(
        Bucket, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.job_todo
