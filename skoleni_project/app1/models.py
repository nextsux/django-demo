from django.db import models


CUSTOMER_GENDER_CHOICES = (
    ('M', 'Muz'),
    ('F', 'Zena'),
)


class Customer(models.Model):
    gender = models.CharField(max_length=1, verbose_name='pohlavi', choices=CUSTOMER_GENDER_CHOICES)
    name = models.CharField(max_length=255, verbose_name='jmeno zakaznika')
    surname = models.CharField(max_length=255, verbose_name='prijmeni')
    nickname = models.CharField(max_length=255, verbose_name='prezdivka', null=True, blank=True)
    email = models.EmailField(verbose_name='e-mail')

    def get_vek(self):
        return 18

    class Meta:
        verbose_name = 'zakaznik'
        verbose_name_plural = 'zakaznici'
