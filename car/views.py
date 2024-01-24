from rest_framework import viewsets
from .models import BrandCategory, ModelCategory, YearCategory, BodyTypeCategory, ImageCategory, EngineCategory, \
    DriveUnitCategory, TransmissionCategory, ModificationCategory, SteeringWheelCategory, CarAds, ImgCategory
from .serializers import BrandCategorySerializer, ModelCategorySerializer, YearCategorySerializer, \
    BodyTypeCategorySerializer, ImageCategorySerializer, EngineCategorySerializer, DriveUnitCategorySerializer, \
    TransmissionCategorySerializer, ModificationCategorySerializer, SteeringWheelCategorySerializer, CarAdsSerializer, \
    ImgCategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from car.service import PaginationCar


class BrandCategoryViewSet(viewsets.ModelViewSet):
    queryset = BrandCategory.objects.all()
    serializer_class = BrandCategorySerializer
    pagination_class = PaginationCar


class ModelCategoryViewSet(viewsets.ModelViewSet):
    queryset = ModelCategory.objects.all()
    serializer_class = ModelCategorySerializer
    pagination_class = PaginationCar


class YearCategoryViewSet(viewsets.ModelViewSet):
    queryset = YearCategory.objects.all()
    serializer_class = YearCategorySerializer
    pagination_class = PaginationCar


class BodyTypeCategoryViewSet(viewsets.ModelViewSet):
    queryset = BodyTypeCategory.objects.all()
    serializer_class = BodyTypeCategorySerializer
    pagination_class = PaginationCar


class ImageCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
    pagination_class = PaginationCar


class EngineCategoryViewSet(viewsets.ModelViewSet):
    queryset = EngineCategory.objects.all()
    serializer_class = EngineCategorySerializer
    pagination_class = PaginationCar


class DriveUnitCategoryViewSet(viewsets.ModelViewSet):
    queryset = DriveUnitCategory.objects.all()
    serializer_class = DriveUnitCategorySerializer
    pagination_class = PaginationCar


class TransmissionCategoryViewSet(viewsets.ModelViewSet):
    queryset = TransmissionCategory.objects.all()
    serializer_class = TransmissionCategorySerializer
    pagination_class = PaginationCar


class ModificationCategoryViewSet(viewsets.ModelViewSet):
    queryset = ModificationCategory.objects.all()
    serializer_class = ModificationCategorySerializer
    pagination_class = PaginationCar


class SteeringWheelCategoryViewSet(viewsets.ModelViewSet):
    queryset = SteeringWheelCategory.objects.all()
    serializer_class = SteeringWheelCategorySerializer
    pagination_class = PaginationCar


class ImgCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImgCategory.objects.all()
    serializer_class = ImgCategorySerializer
    pagination_class = PaginationCar


class CarAdsViewSet(viewsets.ModelViewSet):
    queryset = CarAds.objects.all()
    serializer_class = CarAdsSerializer
    pagination_class = PaginationCar
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'model', 'year_of_issue', 'body_type', 'image', 'engine', 'drive_unit', 'transmission', 'modification', 'steering_wheel', 'draft']
    search_fields = ['brand__brand', 'model__model', 'year_of_issue__year_of_issue', 'body_type__body_type', 'image__image', 'engine__engine', 'drive_unit__drive_unit', 'transmission__transmission', 'modification__modification', 'steering_wheel__steering_wheel', 'draft']



