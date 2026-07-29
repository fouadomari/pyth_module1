from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ai.content.content_serves import summarize_post

from ai.content.service.summarize import summarize_post_by_id


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