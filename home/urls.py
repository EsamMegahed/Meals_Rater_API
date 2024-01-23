from django.urls import path,include
from .views import MealViewsets,RatingViewsets
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()
router.register('meals',MealViewsets)
router.register('rating',RatingViewsets)


urlpatterns = [
    path('',include(router.urls)),
    path('tokenrequest/',obtain_auth_token),

]

