from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ("is_in_stock",)
    # list_display_links = ("create_date",)
    list_filter = ()


admin.site.register(Product, ProductAdmin)

admin.site.site_title = "Admin Title"
admin.site.site_header = "Hasan Admin Portal"
admin.site.index_title = "Welcome to Hasan Admin Portal"