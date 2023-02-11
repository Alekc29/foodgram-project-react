from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор публикации',
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/'
    )
    description = models.TextField('Текстовое описание')
    ingredients = models.TextField()
    tags = models.CharField(max_length=50)
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[MinValueValidator(1, message='Минимальное значение 1!')]
    )