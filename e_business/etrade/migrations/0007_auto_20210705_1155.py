# Generated by Django 3.1.3 on 2021-07-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0006_auto_20210705_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sc_handle',
            field=models.CharField(blank=True, default='man', max_length=100, null=True),
        ),
    ]