from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre=models.CharField(max_length=255,null=False,blank=False, verbose_name="Empresa")
    domicilio=models.CharField(max_length=255,verbose_name="Domicilio")
    email=models.CharField(max_length=255, verbose_name="Email",blank=False, null=False)
    responsable=models.CharField(max_length=255, verbose_name="Responsable",blank=True,null=True)
    telefono=models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.nombre, self.domicilio, self.email, self.responsable, self.telefono)
    
    class Meta:
        db_table = 'empresa'
        ordering = ["nombre"]
        verbose_name_plural = "Empresa"
        verbose_name = 'Empresa'
        managed=True

class UsuarioSistema(models.Model):
    username=models.CharField('Nombre de Usuario', max_length=10, unique=True)
    email=models.EmailField('Correo Electrónico',unique=True,max_length=255)
    nombre=models.CharField('Nombre',max_length=100, blank=True, null=True)
    apellidos=models.CharField('Apellidos',max_length=100, blank=True,null=True)
    empresa=models.ForeignKey('Empresa',null=True,blank=True,on_delete=models.CASCADE)
        
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email','nombre','apellidos']

    def __str__(self):
        return '%s,%s,%s,%s,%s' %s (self.id, self.username, self.nombre, self.apellidos, self.email, self.empresa)
    class Meta:
        db_table='usuarioSistema'
        ordering = ["nombre"]
        verbose_name_plural = "Usuario_Sistema"
        verbose_name = 'UsuarioSistema'
        managed=True
        
class TipoDocumento(models.Model):
    detalle=models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return '%s,%s' % (self.id, self.detalle)
    
    class Meta:
        db_table = 'tipo_documento'
        ordering = ["detalle"]
        verbose_name_plural = "Tipo Documento"
        verbose_name = 'Tipo Documento'
        managed=True
