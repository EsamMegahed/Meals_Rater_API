from django.shortcuts import render
from .serializers import MealSerializer,RatingSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Rating,Meal
from django.contrib.auth.models import User

# Create your views here.


class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            '''
            Create Or Update
            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                rating = Rating.objects.get(user=user.id,meal=meal.id)
                rating.stars=stars
                rating.save()
                serializer = RatingSerializer(rating,many=False)
                json = {
                    'message':'Meal Rate Update',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_400_BAD_REQUEST)
            
            except:
                rating = Rating.objects.create(meal=meal,user=user,stars=stars)


        return 
        

class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer