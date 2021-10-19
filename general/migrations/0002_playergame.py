# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-08 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Player')),
                ('team', models.CharField(max_length=50, verbose_name='Tm')),
                ('location', models.CharField(max_length=50, verbose_name='H-A')),
                ('opp', models.CharField(max_length=50, verbose_name='Vs')),
                ('game_result', models.CharField(choices=[('W', 'Win'), ('L', 'Loss')], max_length=50, verbose_name='W-L')),
                ('mp', models.FloatField(verbose_name='MP')),
                ('fg', models.IntegerField(verbose_name='FG')),
                ('fga', models.IntegerField(verbose_name='FGA')),
                ('fg_pct', models.FloatField(blank=True, null=True, verbose_name='FG%')),
                ('fg3', models.IntegerField(verbose_name='3P')),
                ('fg3a', models.IntegerField(verbose_name='3PA')),
                ('fg3_pct', models.FloatField(blank=True, null=True, verbose_name='3P%')),
                ('ft', models.IntegerField(verbose_name='FT')),
                ('fta', models.IntegerField(verbose_name='FTA')),
                ('ft_pct', models.FloatField(blank=True, null=True, verbose_name='FT%')),
                ('trb', models.IntegerField(verbose_name='REB')),
                ('ast', models.IntegerField(verbose_name='AST')),
                ('stl', models.IntegerField(verbose_name='ST')),
                ('blk', models.IntegerField(verbose_name='BLK')),
                ('tov', models.IntegerField(verbose_name='TO')),
                ('pf', models.IntegerField(verbose_name='PF')),
                ('pts', models.IntegerField(verbose_name='PTS')),
                ('fpts', models.FloatField(default=-1, verbose_name='FPTS')),
                ('date', models.DateField()),
            ],
        ),
    ]
