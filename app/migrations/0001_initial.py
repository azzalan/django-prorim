# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 00:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceDisponibilidadeMaquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('identificador', models.CharField(max_length=150, verbose_name='Identificador')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de disponibilidade para máquina',
                'verbose_name_plural': 'Opções de disponibilidade para máquina',
            },
        ),
        migrations.CreateModel(
            name='ChoiceExameColeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de exame para controle de coleta',
                'verbose_name_plural': 'Opções de exame para controle de coleta',
            },
        ),
        migrations.CreateModel(
            name='ChoicePeriodoTurno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de período para turno',
                'verbose_name_plural': 'Opções de período para turno',
            },
        ),
        migrations.CreateModel(
            name='ChoiceStatusPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de status para pacientes',
                'verbose_name_plural': 'Opções de status para pacientes',
            },
        ),
        migrations.CreateModel(
            name='ChoiceTesteAgua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de teste de controle de água',
                'verbose_name_plural': 'Opções de teste para controle de água',
            },
        ),
        migrations.CreateModel(
            name='ControleAgua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('resultado', models.BooleanField(default=False, verbose_name='Satisfatório')),
                ('numero_do_laudo', models.IntegerField(default=0, verbose_name='Número do laudo')),
                ('arquivo_resultado', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Arquivo')),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceTesteAgua', verbose_name='Teste')),
            ],
            options={
                'verbose_name': 'Controle de água',
                'verbose_name_plural': 'Controle de água',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='ControleColeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('data_realizado', models.DateTimeField(verbose_name='Data de realização')),
                ('data_envio', models.DateTimeField(verbose_name='Data de envio')),
                ('data_resultado', models.DateTimeField(verbose_name='Data do resultado')),
                ('resultado', models.CharField(max_length=150, verbose_name='Resultado')),
                ('numero_do_laudo', models.IntegerField(verbose_name='Número do laudo')),
                ('realizado', models.BooleanField(default=False, verbose_name='Realizado')),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceExameColeta', verbose_name='Exame')),
            ],
            options={
                'verbose_name': 'Controle de coleta',
                'verbose_name_plural': 'Controle de coleta',
                'ordering': ['-criado'],
            },
        ),
        migrations.CreateModel(
            name='ControleDesinfeccao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('motivo', models.TextField(verbose_name='Motivo')),
                ('realizado', models.BooleanField(default=False, verbose_name='Realizado')),
            ],
            options={
                'verbose_name': 'Controle de desinfecção',
                'verbose_name_plural': 'Controle de desinfecção',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Erro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now_add=True, verbose_name='Última atualização')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('observacao', models.TextField(verbose_name='Observação')),
                ('ocorrido', models.DateTimeField(verbose_name='Ocorrido')),
                ('concluido', models.DateTimeField(verbose_name='Concluído')),
                ('enfermeiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Enfermeiro')),
            ],
            options={
                'verbose_name': 'Erro',
                'verbose_name_plural': 'Erros',
                'ordering': ['-criado'],
            },
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('numero_da_maca', models.IntegerField(verbose_name='Número da maca')),
                ('inicio', models.DateTimeField(verbose_name='Início')),
                ('fim', models.DateTimeField(verbose_name='Fim')),
            ],
            options={
                'verbose_name': 'Estadia',
                'verbose_name_plural': 'Estadias',
                'ordering': ['-inicio', '-criado'],
            },
        ),
        migrations.CreateModel(
            name='ManutencaoCorretiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('acao', models.TextField(blank=True, null=True, verbose_name='Ação')),
                ('erro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manutencao_corretiva', to='app.Erro', verbose_name='Erro')),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Técnico')),
            ],
            options={
                'verbose_name': 'Manutenção corretiva',
                'verbose_name_plural': 'Manutenção corretiva',
                'ordering': ['-criado', '-data'],
            },
        ),
        migrations.CreateModel(
            name='ManutencaoPreventiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('janeiro', models.BooleanField(default=False, verbose_name='Janeiro')),
                ('fevereiro', models.BooleanField(default=False, verbose_name='Fevereiro')),
                ('marco', models.BooleanField(default=False, verbose_name='Março')),
                ('abril', models.BooleanField(default=False, verbose_name='Abril')),
                ('maio', models.BooleanField(default=False, verbose_name='Maio')),
                ('junho', models.BooleanField(default=False, verbose_name='Junho')),
                ('julho', models.BooleanField(default=False, verbose_name='Julho')),
                ('agosto', models.BooleanField(default=False, verbose_name='Agosto')),
                ('setembro', models.BooleanField(default=False, verbose_name='Setembro')),
                ('outubro', models.BooleanField(default=False, verbose_name='Outubro')),
                ('novembro', models.BooleanField(default=False, verbose_name='Novembro')),
                ('dezembro', models.BooleanField(default=False, verbose_name='Dezembro')),
            ],
            options={
                'verbose_name': 'Manutenção preventiva',
                'verbose_name_plural': 'Manutenção preventiva',
            },
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now_add=True, verbose_name='Última atualização')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('fabricante', models.CharField(max_length=150, verbose_name='Fabricante')),
                ('disponibilidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceDisponibilidadeMaquina', verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Máquina',
                'verbose_name_plural': 'Máquinas',
                'ordering': ['erros', 'disponibilidade__identificador', '-criado'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('convenio', models.CharField(max_length=150, verbose_name='Convênio')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceStatusPaciente', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('numero_de_macas', models.IntegerField(verbose_name='Número de macas')),
                ('identificador', models.CharField(max_length=150, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChoicePeriodoTurno', verbose_name='Período')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sala', verbose_name='Sala')),
            ],
            options={
                'verbose_name': 'Seção',
                'verbose_name_plural': 'Seções',
                'ordering': ['-data', '-criado'],
            },
        ),
        migrations.AddField(
            model_name='maquina',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sala', verbose_name='Sala'),
        ),
        migrations.AddField(
            model_name='manutencaopreventiva',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Maquina', verbose_name='Máquina'),
        ),
        migrations.AddField(
            model_name='estadia',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Paciente', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='estadia',
            name='secao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Secao', verbose_name='Seção'),
        ),
        migrations.AddField(
            model_name='erro',
            name='estadia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='erro', to='app.Estadia', verbose_name='Estadia'),
        ),
        migrations.AddField(
            model_name='erro',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='erros', to='app.Maquina', verbose_name='Máquina'),
        ),
    ]
