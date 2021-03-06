# Generated by Django 2.0.5 on 2018-05-30 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180529_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='ist',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='pst',
        ),
        migrations.AddField(
            model_name='schedule',
            name='istslota',
            field=models.CharField(max_length=50, null=True, verbose_name='Time in IST SlotA'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='istslotb',
            field=models.CharField(max_length=50, null=True, verbose_name='Time in IST SlotB'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='pstslota',
            field=models.CharField(max_length=50, null=True, verbose_name='Time in PST SlotA'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='pstslotb',
            field=models.CharField(max_length=50, null=True, verbose_name='Time in PST SlotB'),
        ),
    ]
