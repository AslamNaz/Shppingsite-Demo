# Generated by Django 4.1.4 on 2023-01-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
