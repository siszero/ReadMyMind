# Generated by Django 4.0.4 on 2022-04-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_recommendedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
