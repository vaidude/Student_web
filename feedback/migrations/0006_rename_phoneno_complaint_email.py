# Generated by Django 5.0.3 on 2024-03-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_questions_options_alter_questions_student_dtls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='PhoneNo',
            new_name='email',
        ),
    ]