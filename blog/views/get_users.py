from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer



@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        # Filter for active users only
        active_users = User.objects.filter(is_active=True)
        serializer = UserSerializer(active_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    