# Generated by Django 5.0.1 on 2024-03-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_app', '0003_remove_category_slug_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='content',
            field=models.TextField(default='', max_length=100),
        ),
    ]
