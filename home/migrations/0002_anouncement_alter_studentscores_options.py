# Generated by Django 4.2.8 on 2024-01-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_input', models.CharField(max_length=200)),
                ('date_input', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='studentscores',
            options={'managed': False},
        ),
    ]
