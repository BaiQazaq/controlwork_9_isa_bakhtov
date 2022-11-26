# from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser
from django.db import models


from accounts.managers import UserManager

class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    username = models.CharField(
        verbose_name='Имя',
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars/',
        verbose_name='Аватар'
    )
    
    liked_photo = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='photos.Photo',
        related_name='user_likes',
        blank=True
    )
    commented_photos = models.ManyToManyField(
        verbose_name='Прокомментированные фото',
        to='photos.Photo',
        related_name='user_comments',
        blank=True
    )
    
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        
