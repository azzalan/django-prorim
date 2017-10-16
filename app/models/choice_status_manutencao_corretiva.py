from django.db import models
from app.strings import (
    VERBOSE_CRIADO,
    VERBOSE_ATUALIZADO,
    VERBOSE_CHOICE_STATUS_MANUTENCAO_CORRETIVA,
    VERBOSE_PLURAL_CHOICE_STATUS_MANUTENCAO_CORRETIVA,
    VERBOSE_NOME,
    VERBOSE_DESATIVADO,
)


class ChoiceStatusManutencaoCorretiva(models.Model):
    """ Opções de status para manutenção corretiva. """

    class Meta:
        verbose_name = VERBOSE_CHOICE_STATUS_MANUTENCAO_CORRETIVA
        verbose_name_plural = VERBOSE_PLURAL_CHOICE_STATUS_MANUTENCAO_CORRETIVA

    criado = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=VERBOSE_CRIADO,
    )
    atualizado = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name=VERBOSE_ATUALIZADO,
    )
    nome = models.CharField(
        max_length=150,
        verbose_name=VERBOSE_NOME,
    )
    desativado = models.BooleanField(
        default=False,
        verbose_name=VERBOSE_DESATIVADO,
    )

    def __str__(self):
        return str(self.nome)