# Generated by Django 5.1 on 2024-08-22 19:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0002_category_transaction"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-date"]},
        ),
    ]
