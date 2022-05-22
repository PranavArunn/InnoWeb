from django.db import models

# Create your models here.
class New_model(models.Model):
    Word  = models.CharField(max_length = 100)
    def __str__(self):
        return self.Word
    Content = models.TextField(max_length = 300000)
    def __str__(self):
        return self.Content

class New_feedback(models.Model):
    feedback1 = models.CharField(max_length= 20)
    def __str__(self):
        return self.feedback1
    feedback2 = models.CharField(max_length= 20)
    def __str__(self):
        return self.feedback2
