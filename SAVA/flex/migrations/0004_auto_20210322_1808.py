# Generated by Django 3.1.7 on 2021-03-22 18:08

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_auto_20210322_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add some text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True),
        ),
    ]