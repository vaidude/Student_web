# Generated by Django 5.0.3 on 2024-03-27 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='student_dtls',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feedback.student'),
            preserve_default=False,
        ),
    ]
