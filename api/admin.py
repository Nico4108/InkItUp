from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Tattoo, Artist, Appointment, Ink, ParlorHasInk, ProducerHasSupplier, Producer, Supplier, TattooHasInk, Tattooparlor
# Register your models here.

# admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Tattoo)
admin.site.register(Appointment)
admin.site.register(Artist)
admin.site.register(Ink)
admin.site.register(ParlorHasInk)
admin.site.register(Producer)
admin.site.register(ProducerHasSupplier)
admin.site.register(Supplier)
admin.site.register(TattooHasInk)
admin.site.register(Tattooparlor)