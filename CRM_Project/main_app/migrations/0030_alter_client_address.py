# Generated by Django 4.1.4 on 2022-12-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_alter_brand_brand_alter_client_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(default='No address', max_length=40, verbose_name='Адрес'),
        ),
    ]
