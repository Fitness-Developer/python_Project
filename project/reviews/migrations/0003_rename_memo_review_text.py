# Generated by Django 5.0.6 on 2024-09-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_delete_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='memo',
            new_name='text',
        ),
    ]