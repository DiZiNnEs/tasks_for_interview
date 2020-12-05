from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ScoreSerializer

from .multiply import get_multiply


class TApiView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        multipliers = serializer.validated_data['multipliers']
        result = get_multiply(multipliers)
        return Response(
            {
                'Введенные данные': multipliers,
                'Результат': result,
            }
        )
