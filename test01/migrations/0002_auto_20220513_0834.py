# Generated by Django 3.2.5 on 2022-05-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='samsung',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='samsung',
            name='date',
            field=models.DateField(db_column='date', unique=True),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='negative',
            field=models.IntegerField(db_column='negative', null=True),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='neutral',
            field=models.IntegerField(db_column='neutral', null=True),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='positive',
            field=models.IntegerField(db_column='positive', null=True),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='price',
            field=models.IntegerField(db_column='price', null=True),
        ),
        migrations.AlterModelTable(
            name='samsung',
            table='samsung',
        ),
    ]