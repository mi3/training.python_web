from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Publish selected posts"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(status='d')
make_unpublished.short_description = "Unpublish selected posts"

class CategoryInline(admin.TabularInline):
    # inlining with many-to-many relationships
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [ CategoryInline, ]
    
    #Add columns for the date fields to the list display of Posts.
    list_display = ('title', 'author', 'created_date', 
                'published_date', 'modified_date', 'status')    

    #For more fun, make this a link that takes you to the admin page for that user.
#    list_display_links = ('author',)  # Well this takes to change-post

    #Display the created and modified dates for your posts 
    #when viewing them in the admin.
    readonly_fields = ('created_date', 'modified_date')

    actions = [make_published, make_unpublished]


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
