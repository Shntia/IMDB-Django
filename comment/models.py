from django.contrib.auth.models import User
from django.db import models


class AbstractComment(models.Model):
    status_choices = (
        (1, 'Created'),
        (2, 'Approved'),
        (3, 'Rejected'),
        (4, 'Deleted'),
    )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    comment_body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)ss')
    status = models.PositiveSmallIntegerField(choices=status_choices, default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
