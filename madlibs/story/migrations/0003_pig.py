# Generated by Django 2.2 on 2023-07-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_storyinfo_story_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='pig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=50)),
                ('vehicle', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('restaurant', models.CharField(max_length=50)),
                ('porkItem', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]