from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

STATUS_CHOICES = ( 
    ('d', 'Draft'),
    ('p', 'Published'),
)

class Post(models.Model):
	title = models.CharField(max_length=128)
	text = RichTextField(blank=True)
	author = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)

	def __unicode__(self):
		return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, null=True,
                                   related_name='categories')

    #Change the admin index to say 
    #'Categories' instead of 'Categorys'.
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __unicode__(self):
        return self.name
