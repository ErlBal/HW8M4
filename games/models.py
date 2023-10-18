from django.db import models

class Games(models.Model):
    GENRE = (
        ('MMORPG', 'MMORPG'),
        ('Shooter', 'Shooter'),
        ('Strategy', 'Strategy'),
        ('Horror', 'Horror')
    )
    PLATFORM = (
        ('PC', 'PC'),
        ('PS', 'PS'),
        ('Xbox', 'Xbox')
    )
    title = models.CharField('Укажите название игры', max_length=100)
    description = models.TextField('Укажите описание игры')
    image = models.ImageField('Загрузите фото', upload_to='game/')
    cost = models.PositiveIntegerField('Укажите цену')
    year = models.DateField('Укажите дату выпуска игры', null=True)
    publisher = models.CharField('Укажите издателя игры', max_length=100)
    genre = models.CharField('Укажите жанр', max_length=100, choices=GENRE)
    platform = models.CharField('Укажите платформу', max_length=100, choices=PLATFORM)
    trailer = models.URLField('Укажите трейлер', blank=True)
    gameplay = models.URLField('Укажите видео с геймплеем', blank=True)

    def __str__(self):
        return f'{self.title}.{self.genre}'
