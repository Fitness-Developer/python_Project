# Generated by Django 5.1.1 on 2024-12-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_reviewsofproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsofproduct',
            name='memo',
            field=models.TextField(),
        ),
    ]
