# Generated by Django 4.0.3 on 2022-05-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_metalinstance_metal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metalinstance',
            name='Metal_Photo',
            field=models.ImageField(height_field=20, null=True, upload_to='lesotorgov_base_site/catalog/templates/catalog/static/image/Metal', width_field=20),
        ),
    ]