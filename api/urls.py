from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductsList, ProductsDetail, UserCreation, UserDetail, UserList

urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),
    path('products/', ProductsList.as_view(), name="Products"),
    path('products/<int:pk>/', ProductsDetail.as_view(), name="Product-edits"),
    path('customers/', UserList.as_view(), name="Customer"),
    path('customers/<int:pk>/', UserDetail.as_view(), name="Customer-edit"),
    path('register/', UserCreation.as_view(), name="Customer-creation"),
]

urlpatterns = format_suffix_patterns(urlpatterns)