from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


class Appointment(models.Model):
    idappointment = models.IntegerField(db_column='idAppointment', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    sessionlenght = models.IntegerField(db_column='SessionLenght', blank=True, null=True)  # Field name made lowercase.
    customer_cpr = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='Customer_CPR')  # Field name made lowercase.
    tattooparlor_cvr = models.ForeignKey('Tattooparlor', on_delete=models.CASCADE, db_column='Tattooparlor_CVR')  # Field name made lowercase.
    artist_cpr = models.ForeignKey('Artist', on_delete=models.CASCADE, db_column='Artist_CPR')  # Field name made lowercase.

    class Meta:
        db_table = 'appointment'
        unique_together = (('idappointment', 'customer_cpr', 'tattooparlor_cvr'),)


class Artist(models.Model):
    cpr = models.IntegerField(db_column='CPR', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.IntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    tattooparlor_cvr = models.ForeignKey('Tattooparlor', on_delete=models.CASCADE, db_column='Tattooparlor_CVR')  # Field name made lowercase.

    class Meta:
        db_table = 'artist'


class Customer(models.Model):
    cpr = models.IntegerField(db_column='CPR', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.IntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    registered = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'customer'


class Ink(models.Model):
    batchnumber = models.IntegerField(db_column='BatchNumber', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45, blank=True, null=True)  # Field name made lowercase.
    colorcode = models.CharField(db_column='ColorCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    experationdate = models.DateTimeField(db_column='ExperationDate', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    producer_cvr = models.ForeignKey('Producer', on_delete=models.CASCADE, db_column='Producer_CVR')  # Field name made lowercase.

    class Meta:
        db_table = 'ink'
        unique_together = (('batchnumber', 'producer_cvr'),)


class ParlorHasInk(models.Model):
    ink_batchnumber = models.ForeignKey('Ink', on_delete=models.CASCADE, db_column='Ink_batchnumber', blank=True, null=True)  # Field name made lowercase.
    parlor_storageid = models.ForeignKey('Tattooparlor', on_delete=models.CASCADE, db_column='Parlor_storageID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'parlor_has_ink'


class Producer(models.Model):
    cvr = models.IntegerField(db_column='CVR', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.IntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'producer'


class ProducerHasSupplier(models.Model):
    producer_cvr = models.OneToOneField(Producer, on_delete=models.CASCADE, db_column='Producer_CVR', primary_key=True)  # Field name made lowercase.
    supplier_cvr = models.ForeignKey('Supplier', on_delete=models.CASCADE, db_column='Supplier_CVR')  # Field name made lowercase.

    class Meta:
        db_table = 'producer_has_supplier'
        unique_together = (('producer_cvr', 'supplier_cvr'),)


class Supplier(models.Model):
    cvr = models.IntegerField(db_column='CVR', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'supplier'


class Tattoo(models.Model):
    idtattoo = models.AutoField(db_column='idTattoo', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    placementonbody = models.CharField(db_column='PlacementOnBody', max_length=45, blank=True, null=True)  # Field name made lowercase.
    appointment_idappointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, db_column='Appointment_idAppointment')  # Field name made lowercase.

    class Meta:
        db_table = 'tattoo'
        unique_together = (('idtattoo', 'appointment_idappointment'),)


class TattooHasInk(models.Model):
    tattoo_idtattoo = models.OneToOneField(Tattoo, on_delete=models.CASCADE, db_column='Tattoo_idTattoo', primary_key=True)  # Field name made lowercase.
    ink_batchnumber = models.ForeignKey('Ink', on_delete=models.CASCADE, db_column='Ink_BatchNumber')  # Field name made lowercase.

    class Meta:
        db_table = 'tattoo_has_ink'
        unique_together = (('tattoo_idtattoo', 'ink_batchnumber'),)


class Tattooparlor(models.Model):
    cvr = models.IntegerField(db_column='CVR', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=75, blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.IntegerField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    supplier_cvr = models.ForeignKey('Supplier', on_delete=models.CASCADE, db_column='Supplier_CVR')  # Field name made lowercase.
