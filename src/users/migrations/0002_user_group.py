# Generated by Django 4.0.10 on 2023-09-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(choices=[('MA', 'Manager'), ('MO', 'Moderator'), ('EM', 'Employee')], default='EM', max_length=2),
        ),
    ]