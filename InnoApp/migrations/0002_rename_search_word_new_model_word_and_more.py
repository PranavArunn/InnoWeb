# Generated by Django 4.0.4 on 2022-05-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_model',
            old_name='search_word',
            new_name='Word',
        ),
        migrations.AlterField(
            model_name='new_model',
            name='Content',
            field=models.CharField(max_length=300000),
        ),
    ]