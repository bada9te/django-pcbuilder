from django.contrib import admin
from .models import User, GPU, CPU, RAM, Motherboard, Storage, Box, PSU, PcBuild

# Register your models here.
admin.site.register(User)
admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Motherboard)
admin.site.register(Storage)
admin.site.register(Box)
admin.site.register(PSU)
admin.site.register(PcBuild)
