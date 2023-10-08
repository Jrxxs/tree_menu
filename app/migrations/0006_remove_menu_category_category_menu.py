# Generated by Django 4.2.2 on 2023-10-08 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_category_options_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='app.menu'),
        ),
    ]