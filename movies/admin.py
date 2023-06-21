from django.contrib import admin
from .models import Movies

# Register your models here.
class CustomMovieAdmin(admin.ModelAdmin):
    model = Movies
    list_display = ['title', 'description', 'user',]
    fieldsets= (
        ('Owner',{
            'fields':('user',
            )}
        ),
        ('Movie Information',{
            'fields':('title','description',
            )}
        )
    )

admin.site.register(Movies, CustomMovieAdmin)
