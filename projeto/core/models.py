from django.db import models

class Produtos(models.Model):
    name = models.CharField('Nome Produto',max_length=60)
    description = models.TextField('Descrição',max_length=255)
    
    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ['name']
    
    def __str__(self):
        return self.name    