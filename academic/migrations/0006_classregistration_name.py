# Generated by Django 3.0.2 on 2020-01-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20200117_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='classregistration',
            name='name',
            field=models.CharField(default='one/A', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
