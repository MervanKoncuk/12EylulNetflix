# Generated by Django 3.2.12 on 2022-11-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221026_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='videolar/'),
        ),
    ]
