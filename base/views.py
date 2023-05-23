from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Good_or_Bad, Result
from .serializers import GoodOrBadSerializer, ResultSerializer
from better_profanity import profanity
import datetime

class GoodOrBadAPIView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        good_or_bads = Good_or_Bad.objects.all()
        serializer = GoodOrBadSerializer(good_or_bads, many=True)

        today = datetime.date.today()

        year = today.year
        print(year)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request):

        reason = request.data.get('reason') 
        data = {
            "reason": profanity.censor(reason) if reason is not None else "", 
            "is_good_day": request.data.get('is_good_day'), 
        }

        serializer = GoodOrBadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            #Update results table
            result = Result.objects.filter(year=datetime.date.today().year).first()

            if result:
                if request.data.get('is_good_day'):
                    result.good_count += 1
                else: 
                    result.bad_count += 1
                result.save()
            else:
                Result.objects.create(
                    year = datetime.date.today().year,
                    good_count = 0 if not request.data.get('is_good_day') else 1,
                    bad_count = 1 if not request.data.get('is_good_day') else 0,
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResultsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    