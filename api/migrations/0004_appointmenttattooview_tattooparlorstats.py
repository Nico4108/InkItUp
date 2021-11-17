# Generated by Django 3.2.9 on 2021-11-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_artiststats'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmenttattooview',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('SessionLenght', models.IntegerField(blank=True, null=True)),
                ('CustomerName', models.CharField(blank=True, max_length=45, null=True)),
                ('TattooparlorName', models.CharField(blank=True, max_length=70, null=True)),
                ('ArtistName', models.CharField(blank=True, max_length=45, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('PlacementOnBody', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'appointmenttattooview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='tattooparlorstats',
            fields=[
                ('Name', models.CharField(max_length=75, primary_key=True, serialize=False, unique=True)),
                ('NumSes', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tattooparlorstats',
                'managed': False,
            },
        ),
    ]
