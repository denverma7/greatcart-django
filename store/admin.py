from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',  'category', 'modified_date', 'is_available') # to show the product name, price, stock, availability, category, created date and modified date fields in admin panel
    prepopulated_fields = {'slug':('product_name',)} # to automatically populate the slug field based on the product name field in admin panel}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)