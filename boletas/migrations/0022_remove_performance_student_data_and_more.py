# Generated by Django 4.2.3 on 2023-08-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletas', '0021_performance_student_data_alter_performance_semana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='student_data',
        ),
        migrations.AddField(
            model_name='performance',
            name='student_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
