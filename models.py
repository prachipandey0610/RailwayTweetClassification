from django.db import models
from django.contrib.auth.models import User

import uuid 


class Tweet(models.Model):
     
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    uid             = models.UUIDField(default = uuid.uuid4, editable = False)
    username        = models.CharField(max_length=500, blank=True, null=True)
    tweet           = models.CharField(max_length=500, blank=True, null=True)
    remark          = models.CharField(max_length=500, blank=True, null=True)

    created         = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user) + ' - ' + self.product_name

    