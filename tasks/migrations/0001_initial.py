# Generated by Django 5.1.6 on 2025-03-12 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                (
                    "name",
                    models.CharField(
                        help_text="Enter the task name or description.", max_length=255
                    ),
                ),
                (
                    "completed",
                    models.BooleanField(
                        default=False, help_text="Is the task completed?"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The time when the task was created.",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The time when the task was last updated.",
                    ),
                ),
            ],
        ),
    ]
