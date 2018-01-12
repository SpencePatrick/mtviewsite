# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-12-26 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=60)),
                ('amountneeded', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amountraised', models.DecimalField(decimal_places=2, max_digits=8)),
                ('picture', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Contributors',
            new_name='Contributor',
        ),
        migrations.RenameModel(
            old_name='Roster',
            new_name='Wrestler',
        ),
        migrations.RenameModel(
            old_name='Matches',
            new_name='WrestlingMatch',
        ),
        migrations.DeleteModel(
            name='Budgets',
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributedto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtview.Budget'),
        ),
        migrations.AddField(
            model_name='budget',
            name='budgetcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtview.BudgetCategory'),
        ),
    ]