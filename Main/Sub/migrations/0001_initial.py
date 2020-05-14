# Generated by Django 3.0.6 on 2020-05-14 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('Updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('CategoryName', models.CharField(max_length=255, verbose_name='CategoryName')),
            ],
            options={
                'verbose_name': 'PostCategory',
                'verbose_name_plural': 'PostCategories',
                'ordering': ['CategoryName'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Contents', models.TextField(max_length=1000)),
                ('Created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('Published_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Published at')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('Author_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('PostCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sub.PostCategory', verbose_name='PostCategory')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-Created_at'],
            },
        ),
    ]
