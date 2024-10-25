from django.contrib import admin

# Register your models here.

from banking.models import Customer
from banking.models import Branch


admin.site.register(Customer)
admin.site.register(Branch)
