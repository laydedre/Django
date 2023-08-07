from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50,null=False,blank=False,verbose_name='Categoria')
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0,verbose_name='Valor do planejamento')
    
    def __str__(self):
        return self.categoria

class Conta(models.Model):
    banco_choises = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Economica'),
        ('BR', 'Bradesco'),
        ('IU', 'Itau Unibanco'),
        ('ST', 'Santander'),
        ('PP', 'PicPay'),
        ('BI', 'Banco Inter'),
        ('BP', 'Banco PAN'),
        ('BN', 'Banco Neon'),
        ('BC', 'Banco C6 Bank')
    )
    
    tipo_choises = (
        ('pf', 'Pessoa Fisica'),
        ('pj', 'Pessoa Juridica'),
    )
    
    apelido = models.CharField(max_length=50, blank=False)
    banco =  models.CharField(max_length=2,choices=banco_choises)
    tipo = models.CharField(max_length=2,choices=tipo_choises)
    valor = models.FloatField
    icone = models.ImageField(upload_to='Icone')
    
    def __str__(self):
        return self.apelido