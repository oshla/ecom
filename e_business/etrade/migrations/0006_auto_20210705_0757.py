# Generated by Django 3.1.3 on 2021-07-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0005_auto_20210703_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]