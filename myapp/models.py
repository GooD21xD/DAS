from django.db import models

# Create your models here.

class usuario(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha = models.DateField()
    class Meta:
        app_label = 'myapp'

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha = models.DateField()
    # class Meta:
    #     app_label = 'myapp'  

class Activaciones(models.Model):
    cliente = models.CharField(max_length=255)
    documento = models.IntegerField(primary_key=True)  # Cambio a IntegerField
    correo = models.CharField(max_length=255)
    telefono = models.IntegerField(null=True)  # Cambio a IntegerField
    direccion = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    # fec_activacion = models.DateTimeField(null=True)  # Puedes usar DateField si solo necesitas la fecha
    fec_activacion = models.DateField(null=True)  # Cambio a DateField

    def formatted_fecha_activacion(self):
        return self.fec_activacion.strftime('%d/%m/%Y') if self.fec_activacion else None

    class Meta:
        db_table = 'activaciones'

class Facturacion(models.Model):
    cliente = models.CharField(max_length=255)
    documento = models.IntegerField(primary_key=True)  # Cambio a IntegerField para que sea entero
    correo = models.CharField(max_length=255)
    telefono = models.IntegerField(null=True)  # Cambio a IntegerField para que sea entero
    plan = models.CharField(max_length=255)
    ciclo_facturacion = models.IntegerField(null=True)
    monto = models.FloatField(null=True)
    fec_facturacion = models.DateField(null=True)

    def formatted_fecha_facturacion(self):
        return self.fec_facturacion.strftime('%d/%m/%Y') if self.fec_facturacion else None

    class Meta:
        db_table = 'facturacion'