# Generated by Django 3.0.3 on 2020-02-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAllFormTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_char_field', models.CharField(max_length=200)),
                ('a_date_time_field', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]