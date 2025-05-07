from django.db import models

class News_post(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.CharField('Описание', max_length=255)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор', max_length=100)

    def __str__(self):
        return self.title
