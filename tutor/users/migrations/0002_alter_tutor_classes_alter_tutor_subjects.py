# Generated by Django 4.0.6 on 2022-07-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='classes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='subjects',
            field=models.TextField(),
        ),
    ]