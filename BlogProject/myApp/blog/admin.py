from django.contrib import admin
from .models import Category, Post
# Register your models here.


# for configuration of Category Admin

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('image_tag','title', 'description', 'url', 'add_date')
  search_fields = ('title',)
  

# for post confisuration
class PostAdmin(admin.ModelAdmin):
  list_display = ('image_tag', 'title', 'url', 'cat' )
  search_fields = ('title',)
  list_filter = ('cat',)
  list_per_page = 50
  
  class Media:
    js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/7/tinymce.min.js', 'js/script.js')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)