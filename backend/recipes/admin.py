from django.contrib.admin import ModelAdmin, register

from recipes.models import (Favorite,
                            Ingredient,
                            Recipe,
                            IngredientInRecipe,
                            ShoppingCart, Tag)


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'color', 'slug')


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'author', 'favorite')
    list_filter = ('name', 'author')
    search_fields = ('name',)
    readonly_fields = ('favorite',)
    fields = ('image',
              ('name', 'author'),
              'text',
              ('tags', 'cooking_time'),
              'favorite')


@register(IngredientInRecipe)
class IngredientInRecipeAdmin(ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('recipe', 'user')


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = ('recipe', 'user')