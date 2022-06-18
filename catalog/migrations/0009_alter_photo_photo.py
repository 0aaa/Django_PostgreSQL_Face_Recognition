# Generated by Django 4.0.5 on 2022-06-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_photo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(help_text="Enter a person's photo", max_length=50, upload_to='catalog'),
        ),
    ]
