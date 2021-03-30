# Generated by Django 3.1.7 on 2021-03-22 20:20

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_auto_20210322_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add some text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock()), ('service_cards', wagtail.core.blocks.StructBlock([('service_title', wagtail.core.blocks.CharBlock(help_text='Add Title', required=True)), ('service_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('service_card_icon', wagtail.images.blocks.ImageChooserBlock()), ('service_title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('service_item', wagtail.core.blocks.TextBlock(max_length=75, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Link to page on your website', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Link to EXTERNAL URL', required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Button Text', max_length=45, required=True))]))], blank=True, null=True),
        ),
    ]
