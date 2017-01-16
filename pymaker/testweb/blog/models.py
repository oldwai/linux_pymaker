from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
	ordering = ('-timestamp',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    search_fields = ('title','timestamp')
class User_login(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	#email = models.CharField(max_length=50)
admin.site.register(BlogPost,BlogPostAdmin)
#admin.site.register(BlogPostAdmin)
#admin.site.register(User_login)
