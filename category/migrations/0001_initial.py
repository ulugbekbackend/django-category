# Generated by Django 4.1.4 on 2023-04-08 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Submenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='category.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Menusub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='category.submenu')),
            ],
        ),
    ]
