from rest_framework.views import Request, Response, APIView, status

class ArticlesViews(APIView):
    def post(self, req: Request) -> Response:
        return Response({"msg: post criado"}, status.HTTP_201_CREATED)
