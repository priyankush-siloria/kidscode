# Generated by Django 2.0.5 on 2018-05-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180529_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='pemail',
            field=models.EmailField(max_length=254, null=True, verbose_name='Parent Email'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slotb',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SlotB Time'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slotbday',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SlotB day'),
        ),
    ]
