from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from car.views import (
    BrandCategoryViewSet, ModelCategoryViewSet, YearCategoryViewSet,
    BodyTypeCategoryViewSet, ImageCategoryViewSet, EngineCategoryViewSet,
    DriveUnitCategoryViewSet, TransmissionCategoryViewSet,
    ModificationCategoryViewSet, SteeringWheelCategoryViewSet, CarAdsViewSet, ImgCategoryViewSet
)
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r'brands', BrandCategoryViewSet)
router.register(r'models', ModelCategoryViewSet)
router.register(r'years', YearCategoryViewSet)
router.register(r'bodytypes', BodyTypeCategoryViewSet)
router.register(r'images', ImageCategoryViewSet)
router.register(r'engines', EngineCategoryViewSet)
router.register(r'driveunits', DriveUnitCategoryViewSet)
router.register(r'transmissions', TransmissionCategoryViewSet)
router.register(r'modifications', ModificationCategoryViewSet)
router.register(r'steeringwheels', SteeringWheelCategoryViewSet)
router.register(r'img-categories', ImgCategoryViewSet)
router.register(r'carads', CarAdsViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
    path('api/auth/', include("rest_framework.urls")),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include("dj_rest_auth.registration.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth-djoser/", include("djoser.urls")),
    path("api/auth-djoser/", include("djoser.urls.authtoken")),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(*urlpatterns, prefix_default_language=False)
