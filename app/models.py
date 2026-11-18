from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('Название', max_length=70)

    def __str__(self):
        return self.title


class Info(models.Model):

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

    year = models.DateField('Год издания')
    pages = models.PositiveIntegerField('Количество страниц')
    country = models.CharField('Страна издания', max_length=50)
    language = models.CharField('Язык издания', max_length=50)

    def __str__(self):
        return str(self.year)


class Book(models.Model):
    RATING = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='book', verbose_name='Категория')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='books/', blank=True, null=True)
    rating = models.CharField('Рейтинг', max_length=1, choices=RATING)
    author = models.CharField('Автор', max_length=70)
    info = models.OneToOneField('Info', on_delete=models.CASCADE, related_name='book', verbose_name='Информация', blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='books', verbose_name='Теги', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title
