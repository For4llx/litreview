# Generated by Django 3.1.4 on 2022-09-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
