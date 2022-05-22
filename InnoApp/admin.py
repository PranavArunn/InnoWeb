from django.contrib import admin

# Register your models here.
from .models import New_feedback, New_model
admin.site.register(New_model)
admin.site.register(New_feedback)
