from django.contrib import admin
from .models import Admin, NaturalPerson, Course, Coevaluation

admin.site.register(Admin)
admin.site.register(NaturalPerson)
admin.site.register(Course)
admin.site.register(Coevaluation)
