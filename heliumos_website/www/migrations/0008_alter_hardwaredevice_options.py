# Generated by Django 5.0 on 2024-09-19 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_hardwaredevice_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwaredevice',
            options={'ordering': ['vendor', 'form_factor', 'name']},
        ),
    ]