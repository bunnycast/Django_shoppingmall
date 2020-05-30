# Generated by Django 3.0.6 on 2020-05-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Register Date')),
                ('fcuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.Fcuser', verbose_name='User')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'db_table': 'fastcampus_order',
            },
        ),
    ]