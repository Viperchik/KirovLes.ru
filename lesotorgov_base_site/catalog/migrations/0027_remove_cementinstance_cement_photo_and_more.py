# Generated by Django 4.0.3 on 2022-05-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_lumber_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cementinstance',
            name='Cement_Photo',
        ),
        migrations.RemoveField(
            model_name='lumberinstance',
            name='Lumber_Photo',
        ),
        migrations.RemoveField(
            model_name='metalinstance',
            name='Metal_Photo',
        ),
    ]
