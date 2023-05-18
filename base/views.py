from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Good_or_Bad
from .serializers import GoodOrBadSerializer

class GoodOrBadAPIView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        good_or_bads = Good_or_Bad.objects.all()
        serializer = GoodOrBadSerializer(good_or_bads, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request):

        # pf = ProfanityFilter()

        # data = {
        #     "reason": pf.censor(request.data.get('reason')) if request.data.get('reason') is not None else "", 
        #     "is_good_day": request.data.get('is_good_day'), 
        # }
        
        reason = request.data.get('reason') 
        data = {
            "reason": reason if reason is not None else "", 
            "is_good_day": request.data.get('is_good_day'), 
        }

        serializer = GoodOrBadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)