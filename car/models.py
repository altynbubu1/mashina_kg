from django.db import models
from django.utils.translation import gettext_lazy as _

from config import settings


#
#
# YEAR_CHOICES = [(i, str(i)) for i in range(1900, 2025)]
#
#
# class Car(models.Model):
#     name = models.CharField(max_length=200, verbose_name="Название")
#     price = models.IntegerField(null=True, blank=True, verbose_name="Цена")
#     currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default="USD", verbose_name="Валюта")
#     year = models.PositiveIntegerField(choices=YEAR_CHOICES, default=2000, verbose_name="Год")
#
#     def __str__(self):
#         return self.name


class BrandCategory(models.Model):
    brand = models.CharField(max_length=200, verbose_name="марка")

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "бренд"
        verbose_name_plural = "бренды"


class ModelCategory(models.Model):
    model = models.CharField(max_length=100, verbose_name="модель")

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "модель"
        verbose_name_plural = "модели"


class YearCategory(models.Model):
    year_of_issue = models.PositiveSmallIntegerField("год выпуска", default=1800)

    def __str__(self):
        return str(self.year_of_issue)

    class Meta:
        verbose_name = "год выпуска"
        verbose_name_plural = "год выпуски"


class BodyTypeCategory(models.Model):
    body_type = models.CharField(max_length=100, verbose_name="Тип кузова")

    def __str__(self):
        return self.body_type

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Тип кузовы"


class ImageCategory(models.Model):
    image = models.ImageField(upload_to="photo", verbose_name="Поколение")

    def __im(self):
        return self.image

    class Meta:
        verbose_name = "Поколение"
        verbose_name_plural = "Поколения"


class EngineCategory(models.Model):
    engine = models.CharField(max_length=100, verbose_name="двигатель")

    def __str__(self):
        return self.engine

    class Meta:
        verbose_name = "двигатель"
        verbose_name_plural = "двигатели"


class DriveUnitCategory(models.Model):
    drive_unit = models.CharField(max_length=100, verbose_name="привод")

    def __str__(self):
        return self.drive_unit

    class Meta:
        verbose_name = "привод"
        verbose_name_plural = "приводы"


class TransmissionCategory(models.Model):
    transmission = models.CharField(max_length=100, verbose_name="Коробка передач")

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробка передачи"


class ModificationCategory(models.Model):
    modification = models.FloatField(verbose_name="модификация")

    def __str__(self):
        return str(self.modification)

    class Meta:
        verbose_name = "модификация"
        verbose_name_plural = "модификации"


class SteeringWheelCategory(models.Model):
    steering_wheel = models.CharField(max_length=100, verbose_name="руль")

    def __str__(self):
        return self.steering_wheel

    class Meta:
        verbose_name = "руль"
        verbose_name_plural = "руль"


class ImgCategory(models.Model):
    img = models.ImageField(upload_to="img", verbose_name="img")

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = "img"
        verbose_name_plural = "img"


class CarAds(models.Model):
    COLOR_RU_CHOICES = (
        ("черный", _("черный")),
        ("белый", _("белый")),
        ("синий", _("синий")),
        ("зеленый", _("зеленый")),
        ("серебристый", _("серебристый")),
        ("серый", _("серый")),
        ("бежевый", _("бежевый")),
        ("бирюзовый", _("бирюзовый")),
        ("бордовый", _("бордовый")),
        ("бронза", _("бронза")),
        ("вишня", _("вишня")),
        ("голубой", _("голубой")),
        ("коричневый", _("коричневый")),
        ("золотистый", _("золотистый")),
        ("жёлтый", _("жёлтый")),
        ("красный", _("красный")),
        ("оранжевый", _("оранжевый")),
        ("розовый", _("розовый")),
        ("сиреневый", _("сиреневый")),
        ("фиолетовый", _("фиолетовый")),
        ("хамелеон", _("хамелеон")),
        ("баклажан", _("баклажан")),
    )

    COLOR_EN_CHOICES = (
        ("black", _("black")),
        ("blue", _("blue")),
        ("red", _("redd")),
    )
    brand = models.ForeignKey(BrandCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_brand", verbose_name="марка")
    model = models.ForeignKey(ModelCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_model", verbose_name="модель")
    year_of_issue = models.ForeignKey(YearCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_year_of_issue", verbose_name="год выпуска")
    body_type = models.ForeignKey(BodyTypeCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_body_type", verbose_name="Тип кузова")
    image = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_image", verbose_name="Поколение")
    engine = models.ForeignKey(EngineCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_engine", verbose_name="двигатель")
    drive_unit = models.ForeignKey(DriveUnitCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_drive_unit", verbose_name="привод")
    transmission = models.ForeignKey(TransmissionCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_transmission", verbose_name="Коробка передач")
    modification = models.ForeignKey(ModificationCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_modification", verbose_name="модификация")
    steering_wheel = models.ForeignKey(SteeringWheelCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="car_ads_steering_wheel", verbose_name="руль")
    draft = models.BooleanField("Черновик", default=False)
    img = models.ManyToManyField(ImgCategory, related_name="car_ads_images", verbose_name="Фотографии")
    #
    link = models.URLField("Ссылка", max_length=200, blank=True, null=True)
    color = models.CharField(choices=COLOR_RU_CHOICES, default=2000, verbose_name="Цвет")
    # color = models.CharField(choices=COLOR_RU_CHOICES if settings.LANGUAGE_CODE == 'ru' else COLOR_EN_CHOICES, default=2000, verbose_name="Цвет")

    def __str__(self):
        return f"{self.brand} {self.model} {self.year_of_issue} - {self.color}"

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "ad"
        verbose_name_plural = "ads"

# second commit
# bootcamp