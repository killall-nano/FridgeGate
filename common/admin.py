from django.contrib import admin

# Register your models here.
from .models import Category, Feedback, Product, Review, Testimony
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Feedback)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','feedback','created_at']
    list_filter = ['name','email','created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_title','approved','first_name','last_name','email','review','created_at','updated_at']
    list_filter = ['first_name','email','review_title','created_at','updated_at']
    search_fields = ('review_title','first_name','last_name','review')
    
@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['name','username','image','user_image']
    list_filter = ['name','username']
    search_fields = ('name','username')

    
admin.site.site_header = "FridgeGate Administration"