from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', GetMethod, basename='product')
router.register('category', CategoryOption, basename='category')
router.register('customers', Customer, basename='customer')
urlpatterns = router.urls

