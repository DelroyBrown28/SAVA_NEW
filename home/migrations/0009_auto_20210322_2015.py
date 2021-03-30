# Generated by Django 3.1.7 on 2021-03-22 20:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('service_cards', wagtail.core.blocks.StructBlock([('service_title', wagtail.core.blocks.CharBlock(help_text='Add Title', required=True)), ('service_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('service_card_icon', wagtail.images.blocks.ImageChooserBlock()), ('service_item_1', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_2', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_3', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_4', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_5', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_6', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_7', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_8', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_9', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('service_item_10', wagtail.core.blocks.TextBlock(max_length=75, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Link to page on your website', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Link to EXTERNAL URL', required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Button Text', max_length=45, required=True))]))], blank=True, null=True),
        ),
    ]
