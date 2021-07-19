from django.db import models


# Create your models here.
class Editorial(models.Model):
    """Quien publica los libros"""
    nombre = models.CharField(max_length=100, help_text="Nombre del editorial")
    pagina_web = models.URLField(help_text="Sitio web")
    email = models.EmailField(help_text="Correo electronico")
