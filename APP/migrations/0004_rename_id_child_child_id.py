# Generated by Django 4.1.5 on 2023-01-14 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_alter_auto_child_id_alter_child_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='id',
            new_name='child_id',
        ),
    ]
