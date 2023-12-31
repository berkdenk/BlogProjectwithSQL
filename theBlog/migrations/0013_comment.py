# Generated by Django 4.2.3 on 2023-10-17 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0012_rename_facebook_profile_fb_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='theBlog.post')),
            ],
        ),
    ]
