# Generated by Django 3.2.9 on 2023-01-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]