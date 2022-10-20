# Generated by Django 4.1.2 on 2022-10-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, '- 0'), (1, '- 1'), (2, '- 2'), (3, '- 3'), (4, '- 4'), (5, '- 5')], default=0),
        ),
    ]
