# Generated by Django 4.1.5 on 2023-03-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_post_title_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title_tag",
            field=models.CharField(max_length=250),
        ),
    ]
