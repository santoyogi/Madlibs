# Generated by Django 2.2 on 2023-07-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_pig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('action1', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('action2', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=50)),
                ('negativeVerb', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('liquid', models.CharField(max_length=50)),
            ],
        ),
    ]
