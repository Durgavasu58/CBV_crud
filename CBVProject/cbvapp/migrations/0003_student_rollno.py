# Generated by Django 3.2.6 on 2021-08-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0002_alter_student_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(default=False),
        ),
    ]
