# Generated by Django 4.1.5 on 2023-04-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0003_teammatesearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammatesearch',
            name='hackathon_name',
            field=models.CharField(default='hackathon team', max_length=255),
        ),
        migrations.AddField(
            model_name='teammatesearch',
            name='phone2',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='teammatesearch',
            name='phone3',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
