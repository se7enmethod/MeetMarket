# Generated by Django 2.2 on 2020-04-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_app', '0003_item_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]