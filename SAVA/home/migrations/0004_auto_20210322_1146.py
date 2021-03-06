# Generated by Django 3.1.7 on 2021-03-22 11:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_main_page_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_page_panels',
            field=wagtail.core.fields.StreamField([('services', wagtail.core.blocks.StructBlock([('service_title', wagtail.core.blocks.CharBlock(help_text="Add the title of the service you're offering", required=True)), ('service_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('service_item', wagtail.core.blocks.TextBlock(max_length=55, required=True))])))]))], blank=True, null=True),
        ),
    ]
