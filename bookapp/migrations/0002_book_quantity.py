# Generated by Django 5.1.7 on 2025-03-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
