# Generated by Django 3.2.8 on 2021-10-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=64)),
                ('news_text', models.TextField(max_length=4096)),
                ('image', models.ImageField(blank=True, upload_to='news_images')),
                ('creating_date', models.DateTimeField(auto_now_add=True)),
                ('counter_of_viewing', models.IntegerField(default=0, editable=False)),
                ('tags', models.ManyToManyField(to='news.Tag')),
            ],
            options={
                'ordering': ['-creating_date'],
            },
        ),
    ]
