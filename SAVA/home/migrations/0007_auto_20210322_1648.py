# Generated by Django 3.1.7 on 2021-03-22 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210322_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_icon',
            new_name='main_page_background_image',
        ),
    ]
