from django.urls import path,include
from .views import MealViewsets,RatingViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meals',MealViewsets)
router.register('rating',RatingViewsets)


urlpatterns = [
    path('',include(router.urls))
]

