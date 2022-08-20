from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Repuestos(models.Model):
    categoria = models.ForeignKey(Categoria, models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    costo_compra = models.FloatField()
    precio_venta = models.FloatField()
    unidades_disponible = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.categoria}'

class Venta(models.Model):
    repuesto = models.ForeignKey(Repuestos, models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateField()
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.repuesto} - {self.cantidad} - {self.fecha_venta}'

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ventas = models.ManyToManyField(Venta)
    estado_de_cuenta = models.FloatField(null=True, blank=True)
    costo_de_inventario = models.FloatField(null=True, blank=True)
    deficit_de_productos = models.CharField(max_length=100, null=True, blank=True)
    # def save(self, *args, **kwargs):
    #     vent = Venta.objects.all()
    #     ventas_delta = vent.filter(fecha_venta__range=[self.fecha_inicio, self.fecha_fin])
    #     # self.ventas.set(ventas_delta)
    #     super(Reporte, self).save(*args, **kwargs)
    #     for p in ventas_delta:
    #         print(p.pk)
    #         self.ventas.add(p.pk)
    #     print(self.ventas)
    #     # self.ventas.add(ventas_delta)
    #     super(Reporte, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.pk}'


@receiver(post_save, sender=Venta)
def guarda_venta(sender, instance, created, **kwargs):
    if created:
        instance.total = instance.cantidad * instance.repuesto.precio_venta
        instance.save()



@receiver(post_save, sender=Reporte)
def guarda_venta(sender, instance, created, **kwargs):
    if created:
        reporte = Reporte.objects.get(pk=instance.pk)
        print(reporte)
        # print(reporte.fecha_fin)
        vent = Venta.objects.all()
        ventas_delta = vent.filter(fecha_venta__range=[instance.fecha_inicio, instance.fecha_fin])
        # print(instance)
        # instance.ventas.add(ventas_delta)
        # print(instance.ventas)
        # print(ventas_delta)
        # reporte.ventas.set(ventas_delta)
        # reporte.save()
        
        # print(reporte.ventas)
        # reporte.ventas.set( ventas_delta)
        # print(reporte.ventas)
        # for p in ventas_delta:
        #     print(p)
        #     reporte.ventas.add(p.pk)
        #     reporte.save()
        # reporte.save()
        # print(reporte.ventas)
        # instance.ventas.set(ventas_delta)
        reporte.ventas.add(*ventas_delta)
        # print(instance.ventas.all())
        print(reporte.ventas.all())
        # reporte.ventas.add(ventas_delta)
        # instance.save()
        reporte.save()
        print(instance)