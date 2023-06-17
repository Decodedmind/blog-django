# Generated by Django 4.1.5 on 2023-03-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(default="uncategorized", max_length=250),
        ),
    ]
