# Generated by Django 3.2.15 on 2023-06-15 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_application_rsvp"),
    ]

    operations = [
        migrations.RemoveField(model_name="application", name="data_agree",),
        migrations.RemoveField(model_name="application", name="gender",),
        migrations.RemoveField(model_name="application", name="q1",),
        migrations.RemoveField(model_name="application", name="q2",),
        migrations.RemoveField(model_name="application", name="q3",),
        migrations.RemoveField(model_name="application", name="rsvp",),
        migrations.AddField(
            model_name="application",
            name="city",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="country",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="devpost",
            field=models.URLField(
                blank=True, help_text="Devpost Profile (Optional)", null=True
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="email_agree",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="I authorize MLH to send me pre- and post-event informational emails, which contain free credit and opportunities from their partners.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="github",
            field=models.URLField(
                blank=True, help_text="Github Profile (Optional)", null=True
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="linkedin",
            field=models.URLField(
                blank=True, help_text="LinkedIn Profile (Optional)", null=True
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="logistics_agree",
            field=models.BooleanField(
                default=False,
                help_text='I authorize you to share my application/registration information with Major League Hacking for event administration, ranking, and MLH administration in-line with the <a href="https://mlh.io/privacy" rel="noopener noreferrer" target="_blank">MLH Privacy Policy</a>. I further agree to the terms of both the <a href="https://github.com/MLH/mlh-policies/blob/main/contest-terms.md" rel="noopener noreferrer" target="_blank">MLH Contest Terms and Conditions</a> and the <a href="https://mlh.io/privacy" rel="noopener noreferrer" target="_blank">MLH Privacy Policy.</a>',
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="program",
            field=models.CharField(
                default="", help_text="Program or Major", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="pronouns",
            field=models.CharField(
                choices=[
                    (None, ""),
                    ("he-him", "he/him"),
                    ("she-her", "she/her"),
                    ("they-them", "they/them"),
                    ("other", "other"),
                    ("no-answer", "prefer not to answer"),
                ],
                default="",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="resume_sharing",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="I consent to IEEE UofT sharing my resume with event sponsors.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="what_past_experience",
            field=models.TextField(
                default=1,
                help_text="If you’ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience.",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="what_technical_experience",
            field=models.TextField(
                default=1,
                help_text="What is your technical experience with software?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="why_participate",
            field=models.TextField(
                default=1,
                help_text="Why do you want to participate in NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="conduct_agree",
            field=models.BooleanField(
                default=False,
                help_text='I have read and agree to the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf" rel="noopener noreferrer" target="_blank">MLH code of conduct</a>.',
            ),
        ),
    ]
