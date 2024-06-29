from django.contrib import admin
from .models import student
from . models import teacher
from . models import hod
from . models import complaint,Questions

#from .models import teacher
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(hod)
admin.site.register(complaint)
admin.site.register(Questions)
