from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models import ImageField


class User(AbstractUser):
    third_name = models.CharField(max_length=200, verbose_name='отчество')
    job = models.CharField(max_length=200, verbose_name='должность')
    department = models.CharField(max_length=200, null=True, verbose_name='подразделение')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.third_name}'

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['first_name']


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['slug']


class Messages(models.Model):
    body = models.TextField(blank=True, verbose_name='сообщение')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,  related_name='messages', verbose_name='отправитель')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sender', verbose_name='получатель')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата отправки')

    def __str__(self):
        return f'{self.body} {self.owner} {self.sender}'
    
    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
        ordering = ['-time_create']


class Equipment(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    place = models.CharField(max_length=200, verbose_name='место утсановки')
    characteristic = models.TextField(blank=True, verbose_name='характеристика')
    cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='category', verbose_name='категория')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.title} {self.place}'
    
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['slug']        


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name='пользователь')
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='comment',  verbose_name='оборудование')
    body = models.TextField(blank=True, verbose_name='комментарий')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.body}'

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_create']        


class Journal(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='journals', verbose_name='оборудование')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='journal', verbose_name='сотрудник')
    body = models.TextField(blank=True, verbose_name='описание ремонта')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.equipment} {self.time_create}'
    
    class Meta:
        verbose_name = 'Журнал ТО/ТР'
        verbose_name_plural = 'Журнал ТО/ТР'
        ordering = ['-time_create'] 