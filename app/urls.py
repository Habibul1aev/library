from django.urls import path, include
from .views import BookViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', BookViewSets)


urlpatterns = [
    path('', include(router.urls)),
    # path('products/', BookViewSets.as_view({'get':'list', 'post':'create'})),
    # path('products/<int:pk>/', BookViewSets.as_view({'get':'retrieve', 'put':'update', 'patch': 'partial_update', 'delete':'destroy'})),
]
