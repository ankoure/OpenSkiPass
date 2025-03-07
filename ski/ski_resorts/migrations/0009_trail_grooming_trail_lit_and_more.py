# Generated by Django 5.1.5 on 2025-03-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski_resorts', '0008_rename_location_skiarea_geom_aerialway_glade_trail'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='grooming',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='trail',
            name='lit',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='aerialway',
            name='aerialway_type',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='aerialway',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aerialway',
            name='detachable',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='aerialway',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aerialway',
            name='occupancy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='glade',
            name='difficulty',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='glade',
            name='name',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='glade',
            name='piste_type',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='difficulty',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='name',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='piste_type',
            field=models.CharField(null=True),
        ),
    ]
