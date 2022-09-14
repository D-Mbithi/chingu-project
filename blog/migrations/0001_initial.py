# Generated by Django 4.1 on 2022-09-04 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("body", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Publish")], max_length=2
                    ),
                ),
                ("publish", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ("-publish",),},
        ),
        migrations.AddIndex(
            model_name="blog",
            index=models.Index(
                fields=["-publish"], name="blog_blog_publish_1d1149_idx"
            ),
        ),
    ]
