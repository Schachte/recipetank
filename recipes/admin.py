from django.contrib import admin
from recipes.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'views')



admin.site.register(Recipe, RecipeAdmin)




