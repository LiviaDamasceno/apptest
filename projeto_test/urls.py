from django.urls import path
from apptest.views import BrandCreateViewSet
from apptest.views import BrandRetrieveUpdateDeleteViewSet
from apptest.views import BrandListViewSet
from apptest.views import RequestTestAPI

urlpatterns = [
    path("api/v1/brand/create", BrandCreateViewSet. as_view(), name="brand_create"),
    
    path("api/v1/brand/<int:pk>/retrieve", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brand_retrieve"),

    path("api/v1/brand/<int:pk>/update", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brands_update"),

    path("api/v1/brand//<int:pk>/destroy", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brand_destroy"),

    path("api/v1/brand/list", BrandListViewSet.as_view(), name="brand_list"),

    path("api/v1/request/", RequestTestAPI.as_view(), name="brand_test"),
]