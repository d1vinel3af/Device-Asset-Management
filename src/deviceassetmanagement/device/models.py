from django.db import models

class DeviceType(models.Model):    
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Тип устройства",
    )
    
    code = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Код типа",
        help_text="Внутренний идентификатор (phone, laptop, monitor, ...)"
    )
    
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    
    class Meta:
        verbose_name = "Тип устройства"
        verbose_name_plural = "Типы устройств"
        ordering = ["name"]
        
    def __str__(self):
        return self.name


class Device(models.Model):
    class Condition(models.TextChoices):
        NEW = "new", "Новое"
        GOOD = "good", "Хорошее"
        SATISFACTORY = "satisfactory", "Удовлетворительное"
        NEEDS_REPAIR = "needs_repair", "Требуется ремонт"
        WRITTEN_OFF = "written_off", "Списано"

    device_type = models.ForeignKey(
        DeviceType,
        on_delete=models.PROTECT,
        related_name="devices",
        verbose_name="Тип устройства"
    )
    
    model = models.CharField(
        max_length=100,
        verbose_name="Модель"
    )
    
    serial_number = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Серийный номер"
    )
    
    purchase_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата покупки"
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name="В эксплуатации"
    )
    
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.GOOD,
        verbose_name="Состояние"
    )
    note = models.TextField(
        blank=True,
        verbose_name="Примечание"
    )

    
    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return f"{self.device_type}:{self.serial_number}:{self.model}"






    