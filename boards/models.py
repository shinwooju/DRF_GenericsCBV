from django.db import models


class Board(models.Model):
    title      = models.CharField(max_length = 100)
    contents   = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'boards'

class Comment(models.Model):
    contents   = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    board      = models.ForeignKey('Board', on_delete = models.CASCADE, related_name = 'comments')

    class Meta:
        db_table = 'comments'