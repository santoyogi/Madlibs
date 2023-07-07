# Generated by Django 2.2 on 2023-07-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=50)),
                ('color1', models.CharField(max_length=50)),
                ('color2', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=50)),
                ('color3', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('verb', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('liquid', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=50)),
                ('adjecitve1', models.CharField(max_length=50)),
                ('actionVerb', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjective1', models.CharField(max_length=50)),
                ('food1', models.CharField(max_length=50)),
                ('verb1', models.CharField(max_length=50)),
                ('verb2', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('hobby', models.CharField(max_length=50)),
                ('food2', models.CharField(max_length=50)),
                ('noun', models.CharField(max_length=50)),
                ('emotion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Closing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('object1', models.CharField(max_length=50)),
                ('object2', models.CharField(max_length=50)),
                ('object3', models.CharField(max_length=50)),
                ('verb', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionVerb', models.CharField(max_length=50)),
                ('noun1', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=50)),
                ('verb', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('noun2', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('adjective3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=50)),
                ('restaurant', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('noun', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('verb', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjective', models.CharField(max_length=50)),
                ('actionVerb1', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('actionVerb2', models.CharField(max_length=50)),
                ('verb', models.CharField(max_length=50)),
                ('noun', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(max_length=50)),
                ('bug', models.CharField(max_length=50)),
                ('adjective1', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('adjective2', models.CharField(max_length=50)),
                ('vegetable', models.CharField(max_length=50)),
                ('adjective3', models.CharField(max_length=50)),
            ],
        ),
    ]
