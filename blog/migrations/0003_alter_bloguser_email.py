# Generated by Django 3.2 on 2021-04-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bloguser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]
