# Generated by Django 5.0.6 on 2024-09-16 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchased', '0002_purchased_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased',
            name='image',
        ),
    ]
