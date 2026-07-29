from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ai.content.content_serves import summarize_post, generate_post

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
    
    
    
@api_view(["POST"])
def summarize_post_view(request):
    post_id = request.data.get("post_id")

    if post_id is None:
        return Response(
            {"error": "post_id is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        result = summarize_post_by_id(post_id)
        return Response(result, status=status.HTTP_200_OK)

    except ValueError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(['POST'])
def generate_post_view(request):
    title = request.data.get('title', '')
    tone = request.data.get('tone')

    try:
        result = generate_post(title, tone)
        return Response(result, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(["POST"])
def summarize_view(request):
    post_id = request.data.get("post_id")

    if not post_id:
        return Response(
            {"error": "post_id is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        result = summarize_post_by_id(post_id)
        return Response(result, status=status.HTTP_200_OK)

    except Exception as exc:
        return Response(
            {"error": str(exc)},
            status=status.HTTP_400_BAD_REQUEST,
        )