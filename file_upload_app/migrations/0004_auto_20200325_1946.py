# Generated by Django 3.0.4 on 2020-03-25 19:46

from django.db import migrations, models
import file_upload_app.models
import file_upload_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload_app', '0003_auto_20200324_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumfile',
            name='image',
            field=models.FileField(upload_to=file_upload_app.models.user_directory_path, validators=[file_upload_app.validators.FileValidator(content_types=('image/jpeg', 'image/gif', 'image/png'), max_size=5000000)]),
        ),
        migrations.AlterField(
            model_name='avatarimage',
            name='image',
            field=models.FileField(upload_to=file_upload_app.models.user_directory_path, validators=[file_upload_app.validators.FileValidator(content_types=('image/jpeg', 'image/gif', 'image/png'), max_size=5000000)]),
        ),
    ]
