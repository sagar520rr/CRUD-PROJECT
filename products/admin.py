from django.contrib import admin
from .models import Product
from django.utils.html import format_html


# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'details', 'display_image', 'price', 'quantity', 'total_price', 'created_date')

    # Method to display the image in the admin list view
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.picture.url))
    
    display_image.short_description = 'Image'  # Column name in the admin

    # Enable search functionality
    search_fields = ('name', 'details')

    # Enable filters
    list_filter = ('created_date', 'price')

# Register the Product model with the custom admin class
admin.site.register(Product, ProductAdmin)
