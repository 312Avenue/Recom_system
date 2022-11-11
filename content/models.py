from django.db import models
from django.contrib.auth import get_user_model


class Content(models.Model):
    GENRE = (
        ('Roman', 'Roman'),
        ('Rap', 'Rap'),
        ('Rock', 'Rock'),
        ('Classic', 'Classic'),
        ('Sience', 'Sience'),
        ('Funny', 'Funny'),
        ('Fantasy', 'Fantasy'),
        ('Entertainment', 'Entertainment'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        )
    title = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=155, verbose_name='Автор')
    album = models.CharField(max_length=155, verbose_name='Альбом')
    img = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Картинка')
    genre = models.CharField(max_length=15, choices=GENRE, verbose_name='Жанр')
    content = models.FileField(verbose_name='Контент', upload_to='file')
    year = models.PositiveSmallIntegerField(verbose_name='Год')

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class Favorites(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author')
    favorites = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='favorites')
    yes_no = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author}: favorites {self.product}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'