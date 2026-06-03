from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)} # to automatically populate the slug field based on the category name field in admin panel
    list_display = ('category_name', 'slug') # to show the category name and slug fields in admin panel

admin.site.register(Category, CategoryAdmin)