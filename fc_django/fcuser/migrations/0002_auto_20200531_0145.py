# Generated by Django 3.0.6 on 2020-05-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=64, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='fcuser',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록날짜'),
        ),
    ]
