# Generated by Django 3.2.25 on 2024-06-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StickyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(choices=[('ffffff', 'White'), ('ffff00', 'Yellow'), ('ff0000', 'Red')], default='ffffff', max_length=6)),
            ],
        ),
    ]