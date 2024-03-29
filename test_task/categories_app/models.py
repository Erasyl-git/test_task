from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='имя категории')

    def __str__(self):
        return f'Имя категории: {self.name}'
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=100, default='')



    def __str__(self):
        return f'Имя подкатегории: {self.name}'
    