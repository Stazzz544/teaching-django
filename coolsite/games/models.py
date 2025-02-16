from django.db import models

# Create your models here.
# тут будут все классы моделей нашего приложения

#поле idпрописывать не нужно, оно автоматически добавляется
class Games(models.Model):
    title = models.CharField(max_length=40) #текстовое поле с макс длиной 40
    content = models.TextField(blank=True) #текстовое поле, с параметром что может быть пустым
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для хранения цены
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')#каталог куда загружать изобрадения
    #каталог photos/тегущий год/текущий месяц/текущий день
    time_create = models.DateTimeField(auto_now_add=True) #автоматически примет текущее значение
    # времени и дальше менятся не будет
    time_update = models.DateTimeField(auto_now=True)#будет менятся каждый раз,при изменении в
    # записи
    is_published = models.BooleanField(default=True)