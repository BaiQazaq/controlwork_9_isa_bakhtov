from django.contrib.auth import get_user_model
from django.db import models
# from django.db.models import TextChoices


class Photo(models.Model):
    sign = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='photos/')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)