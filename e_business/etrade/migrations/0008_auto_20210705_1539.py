# Generated by Django 3.1.3 on 2021-07-05 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0007_auto_20210705_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etrade.customer'),
        ),
    ]
