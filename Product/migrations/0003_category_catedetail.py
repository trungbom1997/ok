# Generated by Django 3.1.7 on 2021-04-01 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20210401_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catedetail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.category'),
        ),
    ]
