# Generated by Django 3.1.5 on 2021-01-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testuser',
            fields=[
                ('idtestuser', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'testuser',
                'managed': False,
            },
        ),
    ]
