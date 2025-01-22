from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=255, verbose_name='Заголовок')
     text = models.TextField(max_length=255, verbose_name='Текст')
     created_date = models.DateTimeField(auto_now_add=True)

     class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

     def __str__(self):
        return self.title