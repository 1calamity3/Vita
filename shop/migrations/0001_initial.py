# Generated by Django 5.1.6 on 2025-02-20 11:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название категории')),
                ('image', models.ImageField(blank=True, default='images/default_item.png', help_text='Необязательно', null=True, upload_to='categories/', verbose_name='Изображение для категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Сохраняется автоматически', verbose_name='Дата и время создания заказа')),
                ('status', models.CharField(choices=[('pending', 'В обработке'), ('in_progress', 'В процессе'), ('completed', 'Выполнен'), ('cancelled', 'Отменен')], default='pending', max_length=20, verbose_name='Статус заказа')),
                ('comment', models.TextField(blank=True, help_text='Необязательно', null=True, verbose_name='Комментарий к заказу')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('type', models.CharField(choices=[('unit', 'Штучно'), ('weight', 'По весу')], max_length=10, verbose_name='Тип продукта')),
                ('description', models.TextField(blank=True, help_text='Необязательно', null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('code', models.CharField(blank=True, help_text='Необязательно', max_length=50, null=True, unique=True, verbose_name='Код продукта')),
                ('stock', models.DecimalField(decimal_places=2, default=0, help_text='Количество товара, которое имеется на складе или на руках', max_digits=10, verbose_name='В стоке')),
                ('image', models.ImageField(blank=True, default='images/default_item.png', help_text='Необязательно', null=True, upload_to='products/', verbose_name='Изображение продукта')),
                ('category', models.ForeignKey(blank=True, help_text='Необязательно', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за ед.')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Предмет заказа',
                'verbose_name_plural': 'Предметы заказа',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, help_text='Необязательно', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.subcategory'),
        ),
    ]
