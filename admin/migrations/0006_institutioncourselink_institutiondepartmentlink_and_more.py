# Generated by Django 5.0.1 on 2024-04-29 16:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0005_remove_course_department"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstitutionCourseLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="admin.course"
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.institution",
                    ),
                ),
            ],
            options={
                "db_table": "institution_course_link",
            },
        ),
        migrations.CreateModel(
            name="InstitutionDepartmentLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.department",
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.institution",
                    ),
                ),
            ],
            options={
                "db_table": "institution_department_link",
            },
        ),
        migrations.AddConstraint(
            model_name="institutioncourselink",
            constraint=models.UniqueConstraint(
                fields=("institution", "course"), name="unique_institution_course_link"
            ),
        ),
        migrations.AddConstraint(
            model_name="institutiondepartmentlink",
            constraint=models.UniqueConstraint(
                fields=("institution", "department"),
                name="unique_institution_department_link",
            ),
        ),
    ]
