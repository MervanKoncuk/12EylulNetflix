# Generated by Django 3.2.12 on 2022-10-31 09:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221031_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
