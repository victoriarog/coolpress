# Generated by Django 4.1.3 on 2022-11-08 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('press', '0002_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gravatar_link', models.URLField()),
                ('github_profile', models.URLField()),
                ('gh_repositories', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]