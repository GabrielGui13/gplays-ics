# Generated by Django 4.0.3 on 2022-03-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Idade', models.IntegerField()),
                ('Apelido', models.CharField(max_length=30)),
                ('Cargo', models.CharField(max_length=30)),
            ],
        ),
    ]