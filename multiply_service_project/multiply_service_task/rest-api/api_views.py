from rest_framework.request import Request
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ScoreSerializer
from .json_handle import get_json_human_readable


class TApiView(APIView):
    def post(self, request: Request, *args, **kwargs) -> json:
        serializer = ScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        first_json = serializer.validated_data['first_json']
        second_json = serializer.validated_data['second_json']
        return Response(
            {
                'Первый JSON': first_json,
                'Второй JSON': second_json,
                'Результат': get_json_human_readable(first_json, second_json)
            }
        )
