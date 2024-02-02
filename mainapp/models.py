from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=64,
        unique=True,

    )
    description = models.TextField(
        verbose_name='описание категории',
        blank=True,

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',

    )
    name = models.CharField(
        verbose_name='Имя продукта',
        max_length=128,

    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое категория',
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание ',
        blank=True,

    )
    print = models.DecimalField(
        verbose_name='цена ',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количесто на складе ',
        default=0,
    )
    created_at = models.DecimalField(
        auto_created=True,
    )
    updated_at = models.DecimalField(
        auto_new=True,
    )

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

