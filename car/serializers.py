from rest_framework import serializers
from .models import BrandCategory, ModelCategory, YearCategory, BodyTypeCategory, ImageCategory, EngineCategory, \
    DriveUnitCategory, TransmissionCategory, ModificationCategory, SteeringWheelCategory, CarAds, ImgCategory

###### account #####
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.first_name
        token["username"] = user.username

        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = CarAds
        fields = "__all__"
        # depth = 1


######
class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategory
        fields = ['brand']


class ModelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCategory
        fields = ['model']


class YearCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = YearCategory
        fields = ['year_of_issue']


class BodyTypeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyTypeCategory
        fields = ['body_type']


class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = ['image']


class EngineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineCategory
        fields = ['engine']


class DriveUnitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveUnitCategory
        fields = ['drive_unit']


class TransmissionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionCategory
        fields = ['transmission']


class ModificationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModificationCategory
        fields = ['modification']


class SteeringWheelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SteeringWheelCategory
        fields = ['steering_wheel']


class ImgCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgCategory
        fields = ['img']


# class CarAdsSerializer(serializers.ModelSerializer):
#     # brand = serializers.PrimaryKeyRelatedField(queryset=BrandCategory.objects.all())
#     img = ImgCategorySerializer(many=True)
#     class Meta:
#         model = CarAds
#         exclude = ("id",)
#         depth = 1

class CarAdsSerializer(serializers.ModelSerializer):
    img = serializers.PrimaryKeyRelatedField(many=True, queryset=ImgCategory.objects.all())

    class Meta:
        model = CarAds
        # exclude = ("id",)
        fields = "__all__"
        # depth = 1
