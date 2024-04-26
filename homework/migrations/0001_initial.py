# Generated by Django 4.2.6 on 2023-10-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('number', models.CharField(max_length=20, verbose_name='телефоннный номер')),
                ('info', models.TextField(verbose_name='информация')),
            ],
            options={
                'verbose_name': ('Про нас',),
                'verbose_name_plural': 'Про участника',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField(verbose_name='ютуб')),
                ('fasebook', models.URLField(verbose_name='фейсбук')),
            ],
            options={
                'verbose_name': ('Контакты',),
                'verbose_name_plural': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_photo', models.ImageField(upload_to='logo_image/', verbose_name='лучшиии фото')),
                ('photos', models.ImageField(upload_to='logo_image/', verbose_name='фото')),
            ],
            options={
                'verbose_name': ('Настройки галереи',),
                'verbose_name_plural': 'Настройка голорея',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_news', models.TextField(verbose_name='Последние новости')),
                ('all_news', models.TextField(verbose_name='Все новости')),
            ],
            options={
                'verbose_name': ('Новости',),
                'verbose_name_plural': 'Новост',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(verbose_name='Посты')),
            ],
            options={
                'verbose_name': ('Посты',),
                'verbose_name_plural': 'Пост',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('login', models.ImageField(upload_to='logo_image/', verbose_name='логотип')),
                ('phone', models.CharField(max_length=200, verbose_name='телефонный номер')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основная настройка',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=30, verbose_name='Команда')),
            ],
        ),
    ]
