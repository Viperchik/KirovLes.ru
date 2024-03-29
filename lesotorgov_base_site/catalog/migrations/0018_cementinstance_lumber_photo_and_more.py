# Generated by Django 4.0.3 on 2022-05-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_lumberinstance_lumber_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cementinstance',
            name='Lumber_Photo',
            field=models.ImageField(null=True, upload_to='lesotorgov_base_site/catalog/templates/catalog/static/image/Cement'),
        ),
        migrations.AddField(
            model_name='metalinstance',
            name='Lumber_Photo',
            field=models.ImageField(null=True, upload_to='lesotorgov_base_site/catalog/templates/catalog/static/image/Metal'),
        ),
        migrations.AlterField(
            model_name='lumberinstance',
            name='Lumber_Photo',
            field=models.ImageField(null=True, upload_to='lesotorgov_base_site/catalog/templates/catalog/static/image/Lumber'),
        ),
    ]
