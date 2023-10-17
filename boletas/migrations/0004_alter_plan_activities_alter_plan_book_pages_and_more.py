# Generated by Django 4.2.3 on 2023-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletas', '0003_alter_plan_activities_alter_plan_book_pages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='activities',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='plan',
            name='book_pages',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plan',
            name='day',
            field=models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday')], max_length=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='expected_learning',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='plan',
            name='resources',
            field=models.TextField(max_length=500),
        ),
    ]