# Generated by Django 3.1.7 on 2021-03-27 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0006_testimonialformpage_testimonial_thank_you_page_bg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonialformpage',
            old_name='testimonial_thank_you_page_bg',
            new_name='testimonial_thank_you_page_background',
        ),
    ]
