from django.db import models

# Create your models here.
class Fcuser(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    password = models.CharField(max_length = 64, verbose_name='password')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='register date')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = 'User'
        verbose_name_plural = 'User'