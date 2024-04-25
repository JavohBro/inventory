# Generated by Django 5.0.3 on 2024-04-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse", "0002_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.IntegerField()),
                ("transaction_type", models.CharField(max_length=10)),
                ("quantity", models.IntegerField()),
                ("customer_id", models.IntegerField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]