# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Personas(models.Model):
    idpersonas = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    edad = models.IntegerField()
    sueldo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'personas'
    

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField(db_column='userId')  # Field name made lowercase.
    title = models.CharField(max_length=45)
    body = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.userId)

   