from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedModel
from .querysets import FilteredQuerySet


User = get_user_model()


class PublishedManager(models.Manager):
    def get_queryset(self):
        return FilteredQuerySet(self.model, using=self._db)


class Category(PublishedModel):
    title = models.CharField(max_length=256,
                             verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True,
                            verbose_name='Идентификатор',
                            help_text=('Идентификатор страницы для URL; '
                                       'разрешены символы латиницы, цифры, '
                                       'дефис и подчёркивание.')
                            )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField(max_length=256,
                            verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text=('Если установить дату и время '
                                               'в будущем — можно делать '
                                               'отложенные публикации.')
                                    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=False,
                               verbose_name='Автор публикации')
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Местоположение')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        return self.title
