# Generated by Django 4.1.5 on 2023-04-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0008_alter_teammatesearch_github1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hacakthon_name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('user_id_rec', models.CharField(max_length=255)),
                ('github_username', models.CharField(max_length=255)),
            ],
        ),
    ]
