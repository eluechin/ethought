# Generated by Django 2.1.7 on 2019-06-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
            preserve_default=False,
        ),
    ]
