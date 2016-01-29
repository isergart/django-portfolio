from django.db import models
from datetime import datetime
from sorl.thumbnail import ImageField


class Customers(models.Model):
    name = models.CharField(max_length=50, verbose_name='заказчик')
    url = models.URLField(max_length=50, help_text='ведите адрес сайта', verbose_name='сайт', blank=True)
    logo = models.ImageField(upload_to='static/portfolio/logo/', verbose_name='логотип', blank=True, help_text='не больше 100 x 100px')

    class Meta:
        db_table = 'portfolio_customer'
        verbose_name = 'заказчика'
        verbose_name_plural = 'заказчики'

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=50, verbose_name='название инструмента')
    logo = models.ImageField(upload_to='static/portfolio/tools/', verbose_name='иконка', blank=True, help_text='не больше 100 x 100px')

    class Meta:
        db_table = 'portfolio_tool'
        verbose_name = 'инструмент'
        verbose_name_plural = 'инструменты'

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('a', 'Дизайн'),
    ('b', 'Живопись'),
    ('d', 'Веб разработка'),
    ('c', 'Фотография'),
    ('e', 'Трехмерная графика'),
    ('f', 'Видео'),
)


# Base class for _django-portfolio project

class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    slug = models.SlugField('URL', unique=True)
    description = models.TextField(blank=True, verbose_name='описание')
    create_date = models.DateField(default=datetime.now, verbose_name='дата создания')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name='категория', default='a')
    status = models.BooleanField(default=True, verbose_name='статус', help_text='Если отмечено, опубликовать проект в сети.')
    slider = models.BooleanField(default=False, verbose_name='слайды', help_text='Если отмечено, изображения отображаются в виде слайдов.')
    comment = models.BooleanField(default=False, verbose_name='комментарии', help_text='Если отмечено, пользователи смогут оставлять свои комментарии.')
    customer = models.ForeignKey(Customers, related_name='customer', verbose_name='заказчик', default=1, on_delete=models.CASCADE)
    tool = models.ManyToManyField(Tools, related_name='tool', verbose_name='инструменты')


    class Meta:
        db_table = 'portfolio_project'
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        ordering = ['-create_date']

    def __str__(self):
        return self.name



class Images(models.Model):
    name = models.CharField(max_length=100, verbose_name='название', blank=True)
    description = models.CharField(max_length=1000, verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='static/portfolio/projects/%Y/%m/%d/'+'%s' % 'foo', verbose_name='изображение',
                        blank=True)
    # img = get_thumbnail(my_file, '100x100', crop='center', quality=99)
    video = models.BooleanField(default=False, verbose_name='видео', help_text='Возможность зарузки видео.')
    project = models.ForeignKey(Projects, related_name='imagefk', verbose_name='галерея', on_delete=models.CASCADE)

    class Meta:
        db_table = 'portfolio_image'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return self.name