# Generated by Django 4.2.3 on 2023-08-13 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletas', '0012_group_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='group',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='boletas.group'),
        ),
    ]
