# Generated by Django 4.1.6 on 2023-02-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('R', "Regular - Can't delete members"), ('A', 'Admin - Can delete members')], max_length=2)),
            ],
        ),
    ]
