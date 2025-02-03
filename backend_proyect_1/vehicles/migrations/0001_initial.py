# Generated by Django 5.1.2 on 2024-12-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('consumption', models.FloatField(verbose_name='consumption(litros/100km)')),
                ('autonomy', models.FloatField(verbose_name='autonomy(km)')),
                ('weight_capacity', models.FloatField(verbose_name='weight_capacity(kg)')),
            ],
        ),
    ]
