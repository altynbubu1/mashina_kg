from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import BrandCategory, ModelCategory, YearCategory, BodyTypeCategory, ImageCategory, EngineCategory, \
    DriveUnitCategory, TransmissionCategory, ModificationCategory, SteeringWheelCategory, CarAds, ImgCategory


class MovieAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    brand = forms.CharField(label="бренд", widget=CKEditorUploadingWidget())

    class Meta:
        model = CarAds
        fields = '__all__'


@admin.register(BrandCategory)
class BrandCategoryAdmin(admin.ModelAdmin):
    list_display = ['brand']


@admin.register(ModelCategory)
class ModelCategoryAdmin(admin.ModelAdmin):
    list_display = ['model']


@admin.register(YearCategory)
class YearCategoryAdmin(admin.ModelAdmin):
    list_display = ['year_of_issue']


@admin.register(BodyTypeCategory)
class BodyTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['body_type']


@admin.register(ImageCategory)
class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(EngineCategory)
class EngineCategoryAdmin(admin.ModelAdmin):
    list_display = ['engine']


@admin.register(DriveUnitCategory)
class DriveUnitCategoryAdmin(admin.ModelAdmin):
    list_display = ['drive_unit']


@admin.register(TransmissionCategory)
class TransmissionCategoryAdmin(admin.ModelAdmin):
    list_display = ['transmission']


@admin.register(ModificationCategory)
class ModificationCategoryAdmin(admin.ModelAdmin):
    list_display = ['modification']


@admin.register(SteeringWheelCategory)
class SteeringWheelCategoryAdmin(admin.ModelAdmin):
    list_display = ['steering_wheel']


@admin.register(ImgCategory)
class ImgCategoryAdmin(admin.ModelAdmin):
    list_display = ['img']


@admin.register(CarAds)
class CarAdsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year_of_issue', 'body_type', 'image', 'engine', 'drive_unit', 'transmission',
                    'modification', 'display_images', 'steering_wheel', 'draft', 'link']
    list_filter = ['brand', 'model']
    form = MovieAdminForm

    def display_images(self, obj):
        return ', '.join([img_category.img.name for img_category in obj.img.all()])

    display_images.short_description = 'Изображения'
