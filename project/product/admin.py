from django.contrib import admin
from .models import Product, CustomUser,ReviewsOfProduct
from django.utils.html import format_html, mark_safe
from django.contrib.admin import site


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image_tag', 'image')
    search_fields = ('title',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "-"


    image_tag.short_description = 'Изображение'

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'value')
    search_fields = ('user__username',)

admin.site.register(ReviewsOfProduct)