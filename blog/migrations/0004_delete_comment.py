# Generated by Django 3.2.9 on 2021-11-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogentry_date_posted'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]