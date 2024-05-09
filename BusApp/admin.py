from django.contrib import admin
from .models import Bus, User, Book

# Register your models here.
admin.site.site_header = "MCA88 Admin"
admin.site.site_title = "MCA88 Admin Portal"
admin.site.index_title = "Welcome to MCA88 Researcher Portal"

admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)


