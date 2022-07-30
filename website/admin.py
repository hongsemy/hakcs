from django.contrib import admin
from .models import Mission, PastEvents, Executive, SectionTitle

# Register your models here.
admin.site.register(Mission)
admin.site.register(PastEvents)
admin.site.register(Executive)
admin.site.register(SectionTitle)