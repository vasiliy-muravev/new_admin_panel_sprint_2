import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    # auto_now_add автоматически выставит дату создания записи
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    # auto_now изменятся при каждом обновлении записи
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    # Типичная модель в Django использует число в качестве id. В таких ситуациях поле не описывается в модели.
    # Вам же придётся явно объявить primary key.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    def __str__(self):
        return self.name

    # Первым аргументом обычно идёт человекочитаемое название поля
    name = models.CharField(_("name"), max_length=255)
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField(_("description"), blank=True)

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = 'content"."genre'
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Person(UUIDMixin, TimeStampedMixin):
    def __str__(self):
        return self.full_name

    # Первым аргументом обычно идёт человекочитаемое название поля
    full_name = models.CharField(_("full_name"), max_length=255)

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = 'content"."person'
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class Filmwork(UUIDMixin, TimeStampedMixin):
    def __str__(self):
        return self.title

    class WorkType(models.TextChoices):
        MOVIE = 'movie'
        TV_SHOW = 'tv_show'

    # Первым аргументом обычно идёт человекочитаемое название поля
    title = models.CharField(_("title"), max_length=255)
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField(_("description"), blank=True)
    # DateField поле даты, не обязательное
    creation_date = models.DateField(_("creation_date"), blank=True)
    # blank=True делает поле необязательным для заполнения.
    file_path = models.TextField(_("file_path"), blank=True)
    # FloatField число с плавающей запятой, не обязательное
    rating = models.FloatField(
        _("rating"),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    # TextChoices выбор из вариантов, обязательное
    type = models.TextField(_('type'), default=WorkType.MOVIE, choices=WorkType.choices)
    genres = models.ManyToManyField(Genre, through="GenreFilmwork")
    persons = models.ManyToManyField(Person, through="PersonFilmwork")

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = 'content"."film_work'
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    class Meta:
        db_table = 'content"."genre_film_work'
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'genre_id'], name='film_work_genre_idx'),
        ]


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.TextField(_("role"))
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    class Meta:
        db_table = 'content"."person_film_work'
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'person', 'role'], name='film_work_person_idx'),
        ]
