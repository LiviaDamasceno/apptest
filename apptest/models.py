from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    id_company = models.IntegerField(null=False, blank=False, verbose_name="Id da empresa", db_column="id_company")
    name_brand = models.CharField(max_length=100, verbose_name="Nome da Marca", null=False, blank=False, db_column="name_brand",)
    enabled = models.CharField(max_length=3, null=False, blank=False, verbose_name="Ativo", db_column="enabled")

    class Meta:
        db_table = "brand"