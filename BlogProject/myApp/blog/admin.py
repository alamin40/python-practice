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



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)