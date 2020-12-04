from rest_framework.views import APIView
from rest_framework.response import Response

from .multiply import get_multiply


class TApiView(APIView):
    def post(self, request, pk, *args, **kwargs) -> Response:
        post_data = [int(x) for x in str(pk)]
        multiply = {"Вы ввели следующие значения": post_data,
                    "Результат": get_multiply(post_data)}
        return Response(multiply)
