# Generated by Django 2.2.9 on 2023-03-15 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0003_auto_20230315_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='author',
            new_name='customer',
        ),
    ]
