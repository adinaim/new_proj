from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewset, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewset, 'prooduct')
router.register('category', CategoryViewSet, 'category')

urlpatterns = [
    path('', include('apps.review.urls'))
]

urlpatterns += router.urls