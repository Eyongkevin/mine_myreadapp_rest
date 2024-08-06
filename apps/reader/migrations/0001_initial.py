# Generated by Django 5.0.7 on 2024-08-05 11:58

import datetime
import django.db.models.deletion
import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="NIC",
            fields=[
                (
                    "nic_number",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("delivery_date", models.DateField()),
                (
                    "expiration_date",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("delivery_date"),
                            "+",
                            models.Value(datetime.timedelta(days=1827)),
                        ),
                        output_field=models.DateField(),
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "NIC",
                "db_table_comment": "National Identity Card",
            },
        ),
        migrations.CreateModel(
            name="Reader",
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
                    "title",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Mr", "Mr"),
                            ("Mrs", "Mrs"),
                            ("Ms", "Ms"),
                            ("Dr", "Dr"),
                        ],
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "nic",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reader",
                        to="reader.nic",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "reader",
            },
        ),
        migrations.AddConstraint(
            model_name="reader",
            constraint=models.CheckConstraint(
                check=models.Q(("title__in", ["Mr", "Mrs", "Ms", "Dr"])),
                name="reader_reader_title_check",
            ),
        ),
    ]
