from django.contrib import admin
from .models import User, Message, Room

admin.register(User)
admin.site.register(Message)
admin.site.register(Room)   
