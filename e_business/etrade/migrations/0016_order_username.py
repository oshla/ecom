# Generated by Django 3.1.3 on 2021-07-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrade', '0015_auto_20210706_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
