# Generated by Django 3.1.3 on 2021-07-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0003_auto_20210702_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='edu_qualification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='marital_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]