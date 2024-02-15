# Generated by Django 5.0.2 on 2024-02-14 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0002_remove_job_category_job_company_job_expiration_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="application",
            name="cover_letter",
        ),
        migrations.AlterField(
            model_name="application",
            name="resume",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="expiration_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 15, 16, 14, 17, 293866, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]