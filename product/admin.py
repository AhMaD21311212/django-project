from django.contrib import admin
from .models import product,Size,Color,Information,Category

class Informationadmin(admin.StackedInline):
    model = Information

@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display = ("title","price")
    prepopulated_fields = {'slug': ('category_name',)}
    inlines = (Informationadmin,)
@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display = ("title","slug","parent")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Size)
admin.site.register(Color)