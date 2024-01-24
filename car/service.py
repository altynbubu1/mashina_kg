from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import CarAds


class PaginationCar(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


# def get_client_ip(request):
#     """Получение IP пользоваеля"""
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
#
#
# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass
#
#
# class CarFilter(filters.FilterSet):
#     brand = CharFilterInFilter(field_name='brand__brand', lookup_expr='in')
#     # model = filters.RangeFilter()
#
#     class Meta:
#         model = Movie
#         fields = ['brand']#, 'model']
