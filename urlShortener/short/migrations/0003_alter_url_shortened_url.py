# Generated by Django 4.0.4 on 2022-05-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_rename_urlstring_url_url_string_url_shortened_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortened_url',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
