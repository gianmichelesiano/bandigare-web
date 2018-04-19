# Generated by Django 2.0.4 on 2018-04-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GareFirebase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDEN', models.CharField(blank=True, max_length=30, null=True)),
                ('IDFIREBASE', models.CharField(max_length=30)),
                ('IDENTIFICATIVO_GARA', models.CharField(blank=True, max_length=30, null=True)),
                ('CIG', models.CharField(blank=True, max_length=30, null=True)),
                ('OGGETTO', models.TextField(blank=True, null=True)),
                ('TIPOLOGIA', models.CharField(blank=True, max_length=30, null=True)),
                ('PROCEDURA', models.CharField(blank=True, max_length=30, null=True)),
                ('ENTE', models.CharField(blank=True, max_length=100, null=True)),
                ('CITTA', models.CharField(blank=True, max_length=100, null=True)),
                ('PROVINCIA', models.CharField(blank=True, max_length=5, null=True)),
                ('REGIONE', models.CharField(blank=True, max_length=30, null=True)),
                ('IMPORTO', models.CharField(blank=True, max_length=50, null=True)),
                ('DATA_PUBBLICAZIONE', models.IntegerField(blank=True, null=True)),
                ('DATA_INSERIMENTO', models.IntegerField(blank=True, null=True)),
                ('DATA_SCADENZA', models.IntegerField(blank=True, null=True)),
                ('CATEGORIA_PREVALENTE', models.CharField(blank=True, max_length=5, null=True)),
                ('CATEGORIE_SCORPORABILI', models.CharField(blank=True, max_length=50, null=True)),
                ('CPV', models.CharField(blank=True, max_length=100, null=True)),
                ('PROVENIENZA', models.CharField(blank=True, max_length=30, null=True)),
                ('DOWNLOAD', models.TextField(blank=True, null=True)),
                ('INFO_AGGIUNTIVE', models.TextField(blank=True, null=True)),
            ],
        ),
    ]