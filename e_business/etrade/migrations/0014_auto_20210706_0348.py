# Generated by Django 3.1.3 on 2021-07-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0013_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampledata',
            name='Mean',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='sampledata',
            name='dist',
            field=models.FloatField(null=True, verbose_name=''),
        ),
    ]
