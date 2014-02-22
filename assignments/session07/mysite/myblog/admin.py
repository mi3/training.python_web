from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class CategoryInline(admin.TabularInline):
    # inlining with many-to-many relationships
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [ CategoryInline, ]
    
    #Add columns for the date fields to the list display of Posts.
    list_display = ('title', 'author', 'created_date', 
                'published_date', 'modified_date')    

    #For more fun, make this a link that takes you to the admin page for that user.
#    list_display_links = ('author',)  # Well this takes to change-post

    #Display the created and modified dates for your posts 
    #when viewing them in the admin.
    readonly_fields = ('created_date', 'modified_date')

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
