# Generated by Django 5.0 on 2024-06-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(help_text='e.g. 0.0.0', max_length=200)),
                ('changelog', models.TextField(help_text='Markdown')),
                ('download_url', models.URLField()),
                ('sha256', models.CharField(max_length=200)),
                ('torrent_url', models.CharField(help_text='Magnet URL', max_length=200)),
                ('is_alpha', models.BooleanField(help_text='Exclusive with is_beta')),
                ('is_beta', models.BooleanField(help_text='Exclusive with is_alpha')),
                ('is_featured', models.BooleanField()),
                ('image_path', models.CharField(help_text='e.g. /www/images/image.png', max_length=200)),
                ('file_size', models.FloatField(help_text='File size in GB')),
                ('release_date', models.DateField(help_text='Date of release')),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
    ]
