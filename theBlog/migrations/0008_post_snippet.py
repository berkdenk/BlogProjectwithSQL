# Generated by Django 4.2.3 on 2023-09-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post...', max_length=255),
        ),
    ]