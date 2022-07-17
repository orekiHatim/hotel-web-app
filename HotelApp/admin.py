from django.contrib import admin
from .models import Rooms, Reservations , Collections , Feedback

admin.site.register(Rooms)
admin.site.register(Reservations)
admin.site.register(Collections)
admin.site.register(Feedback)

# Register your models here.
