# Generated by Django 2.1.7 on 2019-03-15 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FineTip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, unique=True, upload_to='%Y/%m/%d/', verbose_name='preview image')),
                ('license_plate', models.CharField(max_length=6, verbose_name='license plate')),
                ('reason', models.CharField(max_length=100, null=True)),
                ('coordinates', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date found')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'fine tip',
                'verbose_name_plural': 'fine tips',
                'ordering': ('pub_date',),
            },
        ),
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('street_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('coordinates', models.CharField(max_length=200, unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='finetip',
            name='parking_lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onsite.ParkingLot', verbose_name='parking lot'),
        ),
    ]
