from django.db import models
import uuid
# Create your models here.

class RandomUUID(models.Model):
    key = models.DateTimeField(auto_now_add=True)
    value = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    class Meta:
        ordering = ('-key', )

    
    def __str__(self):
        return str(self.value)



