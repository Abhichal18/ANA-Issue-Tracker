# Generated by Django 2.2.5 on 2020-11-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.TextField(default=0, max_length=50),
        ),
    ]
