# Generated by Django 3.2.25 on 2024-06-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticky_app', '0002_rename_created_at_stickynote_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='color',
            field=models.CharField(choices=[('ffffff', 'White'), ('ffff00', 'Yellow'), ('ff0000', 'Red')], default='ffff00', max_length=6),
        ),
    ]
