# Generated by Django 4.1.7 on 2023-08-03 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id_vehicle', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model_vehicle', models.CharField(max_length=255)),
                ('manufacturer_vehicle', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('status', models.CharField(choices=[('N', 'Novo'), ('SM', 'Seminovo'), ('U', 'Usado')], default='N', max_length=3)),
                ('description', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]