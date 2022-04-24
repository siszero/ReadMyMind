# Generated by Django 4.0.3 on 2022-04-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]