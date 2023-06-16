# Generated by Django 3.2.15 on 2023-06-16 01:43

from django.db import migrations, models
import registration.validators


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0009_auto_20230615_2141"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="resume",
            field=models.FileField(
                default=1,
                upload_to="applications/resumes/",
                validators=[
                    registration.validators.UploadedFileValidator(
                        content_types=["application/pdf"], max_upload_size=20971520
                    )
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="what_past_experience",
            field=models.TextField(
                default=1,
                help_text="If you’ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience.",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="what_technical_experience",
            field=models.TextField(
                default=1,
                help_text="What is your technical experience with software?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="why_participate",
            field=models.TextField(
                default=1,
                help_text="Why do you want to participate in NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
    ]
