# Generated by Django 3.2.12 on 2022-08-03 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0007_order_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="hardware",
            name="image_url",
            field=models.CharField(max_length=500, null=True),
        ),
    ]