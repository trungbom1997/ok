# Generated by Django 3.1.7 on 2021-03-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_custome1_customer2_customer3'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custome1',
        ),
        migrations.DeleteModel(
            name='Customer2',
        ),
        migrations.DeleteModel(
            name='Customer3',
        ),
    ]