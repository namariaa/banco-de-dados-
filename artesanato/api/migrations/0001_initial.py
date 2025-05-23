# Generated by Django 5.2.1 on 2025-05-19 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('telefone', models.IntegerField()),
                ('redeSocialLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=500)),
                ('taxa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('valor', models.FloatField()),
                ('tempoPrevisto', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=250)),
                ('nuemero', models.IntegerField()),
                ('bairro', models.CharField(max_length=250)),
                ('cidade', models.CharField(max_length=250)),
                ('estado', models.CharField(max_length=250)),
                ('cep', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Relacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=250)),
                ('parentesco', models.CharField(max_length=250)),
                ('pessoa1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Relacionamento', to='api.cliente')),
                ('pessoa2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('pg', 'pago'), ('op', 'aberto'), ('cc', 'cancelado')], max_length=250)),
                ('descricao', models.CharField(max_length=500)),
                ('valorAssociado', models.FloatField()),
                ('valorTotal', models.FloatField()),
                ('taxaExtra', models.FloatField()),
                ('dataRecebimento', models.DateTimeField()),
                ('dataEntrega', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('formaPagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.formapagamento')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.servico')),
            ],
        ),
    ]
