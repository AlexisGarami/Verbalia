# Generated by Django 4.2.3 on 2023-10-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletas', '0031_alter_plan_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=10),
        ),
    ]