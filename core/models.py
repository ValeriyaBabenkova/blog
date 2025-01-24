from django.db import models
# Create your models here.

class PostCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title
class Post(models.Model):
     title = models.CharField(max_length=255, verbose_name='Заголовок')
     text = models.TextField(max_length=255, verbose_name='Текст')
     created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
     category = models.ForeignKey(PostCategory, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Категория')

     class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_date']

     def __str__(self):
        return self.title

class Feedback(models.Model):
    text = models.TextField(max_length=255, verbose_name='Текст')
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    def __str__(self):
        return self.text
