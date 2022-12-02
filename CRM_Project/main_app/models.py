from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator


class Client(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length=40, verbose_name='Имя')
    surname = models.CharField(max_length=40, verbose_name='Фамилия')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name='Номер телефона')  # Validators should be a list
    address = models.CharField(max_length=40, verbose_name='Адрес')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Brand(models.Model):
    brand = models.CharField(max_length=40, default='No brand', verbose_name='Бренд')

    def __str__(self):
        return f'{self.brand}'


class Model(models.Model):
    model = models.CharField(max_length=40, default='No model', verbose_name='Модель')

    def __str__(self):
        return f'{self.model}'


class UnitType(models.Model):
    unit_type = models.CharField(max_length=28)

    def __str__(self):
        return f'{self.unit_type}'


class Unit(models.Model):
    serial_number = models.CharField(max_length=42, default='No serial', verbose_name='Серийный номер')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='unit', null=True, verbose_name='Бренд')
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name='unit', null=True, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'


class RepairStage(models.Model):
    stage = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.stage}'


class Order(models.Model):
    defect = models.TextField(max_length=120, null=True, blank=True, verbose_name='Описание дефекта')
    diagnostic_result = models.TextField(max_length=400, null=True, blank=True, verbose_name='Результат диагностики')
    works = models.TextField(max_length=500, null=True, blank=True, verbose_name='Выполненные работы')
    finally_price = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True, default=0,
                                        verbose_name='Сумма ремонта')

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='order', verbose_name='Клиент', null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='order', null=True, verbose_name='Техника')
    type_of_unit = models.ForeignKey(UnitType, on_delete=models.PROTECT, related_name='order', null=True, verbose_name='Тип устройства')
    repair_stage = models.ForeignKey(RepairStage, on_delete=models.PROTECT, null=True, related_name='order',
                                     verbose_name='Стадия ремонта')

    def __str__(self):
        return f'{self.pk}'

    def get_url(self):
        return reverse('get-order', args=(self.pk,))
