import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Preco(Base):
    PLANOS_CHOICES = (
        ('PRO', 'PRO'),
        ('PLUS', 'PLUS'),
        ('PREMIUM', 'PREMIUM'),
    )
    ICONE_CHOICES = (
        ('lni-package', 'Box'),
        ('lni-drop', 'Drop'),
        ('lni-star', 'Star'),
    )
    planos = models.CharField('Planos', max_length=50, choices=PLANOS_CHOICES)
    precos = models.DecimalField('Preços', decimal_places=2, max_digits=10)
    icone = models.CharField('Ícone', max_length=50, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.planos


class Avaliacao(Base):
    ICONE_CHOICES = (
        ('lni-star-filled', 'Estrela'),
        ('lni-star-half', 'Estrela 2'),
    )
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb2': {'width': 75, 'height': 75, 'crop': True}})
    icone = models.CharField('Ícone', max_length=50, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOICE = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Laptop-Phone'),
        ('lni-cog', 'Cog'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    )
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    icone = models.CharField('Ícone', max_length=50, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.nome
