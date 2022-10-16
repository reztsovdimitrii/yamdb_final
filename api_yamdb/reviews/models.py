from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import generate_confirmation_code
from .validators import validate_year


class User(AbstractUser):
    """
    Класс для предоставления данных о пользователе.
    """

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]

    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='Информация о себе'
    )
    role = models.CharField(
        max_length=50,
        null=True,
        choices=ROLES,
        verbose_name='Роль',
        default=USER
    )
    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    confirmation_code = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Код подтверждения',
        default=generate_confirmation_code
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=['username', 'email'],
                                    name='uniq_signup'),
        )


class Category(models.Model):
    """Класс для представления списка категорий:
    «Книги», «Фильмы», «Музыка». Может быть расширен администратором.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Класс для представления жанра из списка предустановленных.
    Новые жанры может создавать только администратор.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Класс для представления произведений."""
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True)
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        db_index=True
    )
    name = models.CharField(max_length=200)
    year = models.IntegerField(
        verbose_name='Дата выхода',
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """Класс для представления отзывов и
    оценок на произведения titles от пользователей.
    """
    text = models.TextField()
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Диапазон значений от 1 до 10'),
            MaxValueValidator(10, 'Диапазон значений от 1 до 10')
        ]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique_review')
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Класс для представления комментариев к отзывам."""
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
