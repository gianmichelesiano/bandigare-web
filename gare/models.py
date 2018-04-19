# -*- coding: cp1252 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class GareFirebase(models.Model):
	IDEN	= models.CharField(max_length=30, null=True, blank=True)
	IDFIREBASE	= models.CharField(max_length=30)
	IDENTIFICATIVO_GARA = models.CharField(max_length=30, null=True, blank=True)
	CIG	= models.CharField(max_length=30, null=True, blank=True)
	OGGETTO = 	models.TextField(null=True, blank=True)
	TIPOLOGIA	= models.CharField(max_length=30, null=True, blank=True)
	PROCEDURA	= models.CharField(max_length=30, null=True, blank=True)
	ENTE	= models.CharField(max_length=100, null=True, blank=True)
	CITTA	= models.CharField(max_length=100, null=True, blank=True)
	PROVINCIA	= models.CharField(max_length=5, null=True, blank=True)
	REGIONE	= models.CharField(max_length=30, null=True, blank=True)
	IMPORTO	= models.CharField(max_length=50, null=True, blank=True)
	DATA_PUBBLICAZIONE = models.IntegerField(blank=True, null=True)
	DATA_INSERIMENTO = models.IntegerField(blank=True, null=True)
	DATA_SCADENZA = models.IntegerField(blank=True, null=True)
	CATEGORIA_PREVALENTE = models.CharField(max_length=5, null=True, blank=True)
	CATEGORIE_SCORPORABILI = models.CharField(max_length=50, null=True, blank=True)
	CPV = models.CharField(max_length=100, null=True, blank=True)
	PROVENIENZA = models.CharField(max_length=30, null=True, blank=True)
	DOWNLOAD = models.TextField(null=True, blank=True)
	INFO_AGGIUNTIVE = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.IDFIREBASE