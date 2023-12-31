# Generated by Django 3.2.18 on 2023-08-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='returned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='borrowedbook',
            unique_together={('student', 'book')},
        ),
    ]
