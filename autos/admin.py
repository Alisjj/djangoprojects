from django.contrib import admin
from .models import Auto, Breed, Cat, Make

admin.site.register(Make)
admin.site.register(Auto)
admin.site.register(Breed)
admin.site.register(Cat)

