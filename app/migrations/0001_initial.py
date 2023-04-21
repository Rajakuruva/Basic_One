# Generated by Django 4.2 on 2023-04-18 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('Topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('Topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Spouncer', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]